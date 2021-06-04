from django.urls import path

from main.views import (
    IndexView, AjaxContactView, AjaxHotelView, HotelDetailView, BookingFormView,
    AboutUsView, OurContactView,
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('hotel/<pk>/', HotelDetailView.as_view(), name='hotel_detail'),
    path('booking/', BookingFormView.as_view(), name='booking'),
    path('about-us/', AboutUsView.as_view(), name='about_us'),
    path('our-contact/', OurContactView.as_view(), name='our_contact'),

    path('ajax-contact/', AjaxContactView.as_view(), name='ajax_contact'),
    path('ajax-hotel/<region_id>/', AjaxHotelView.as_view(), name='ajax_hotel'),
]
