from django import forms

from main.models import Contact, Booking


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'text']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'region', 'hotel', 'name', 'phone', 'adult', 'child', 'room',
        ]
