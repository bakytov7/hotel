from datetime import datetime

from django.contrib import messages
from django.db.models import Prefetch
from django.http import JsonResponse
from django.shortcuts import redirect
from django.template import loader
from django.views import generic

from main.forms import ContactForm, BookingForm
from main.models import Hotel, Region, AboutUs, OurContact
from main.utils import (
    prepare_and_send_booking_to_telegram, prepare_and_send_contact_to_telegram,
)


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        rec_list = Hotel.objects.filter(is_recommended=True).order_by('id')
        region_list = (
            Region.objects.all()
            .prefetch_related(
                'hotel_set',
                Prefetch(
                    lookup='hotel_set',
                    queryset=Hotel.objects.filter(is_recommended=True),
                    to_attr='recommended_hotels',
                )
            )
            .order_by('id')
        )
        extra_context = dict(
            region_list=region_list,
            rec_hotels=rec_list,
            contact_form=ContactForm(),
        )
        context.update(extra_context)

        return context


class AjaxContactView(generic.FormView):
    form_class = ContactForm

    def form_valid(self, form):
        contact = form.save()
        prepare_and_send_contact_to_telegram(self.request, contact)
        return JsonResponse({'detail': 'ok'}, status=201)

    def form_invalid(self, form):
        return JsonResponse({'detail': 'not ok'}, status=400)


class AjaxHotelView(generic.ListView):
    queryset = Hotel.objects.all()

    def get(self, request, *args, **kwargs):
        hotel_list = self.queryset.filter(region_id=kwargs.get('region_id'))
        template = loader.get_template('partials/hotel_select.html')
        context = dict(hotel_list=hotel_list)
        response = dict(select_tag=template.render(context=context))
        return JsonResponse(response)


class HotelDetailView(generic.DetailView):
    model = Hotel
    template_name = 'hotel-detail.html'
    context_object_name = 'hotel'


class BookingFormView(generic.CreateView):
    template_name = 'hotel-detail.html'
    form_class = BookingForm

    def form_valid(self, form):
        booking = form.save(commit=False)
        enter_date = self.request.POST['enter_date']
        leave_date = self.request.POST['leave_date']
        booking.enter_date = datetime.strptime(enter_date, '%a %b %d %Y').date()
        booking.leave_date = datetime.strptime(leave_date, '%a %b %d %Y').date()
        booking.save()
        prepare_and_send_booking_to_telegram(self.request, booking)
        messages.success(self.request, 'Заявка успешно отправлено')
        return redirect('index')


class AboutUsView(generic.DetailView):
    model = AboutUs
    template_name = 'info.html'

    def get_object(self, queryset=None):
        return self.model.objects.first()


class OurContactView(generic.DetailView):
    model = OurContact
    template_name = 'info.html'

    def get_object(self, queryset=None):
        return self.model.objects.first()
