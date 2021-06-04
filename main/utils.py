from django.urls import reverse

from main.bot import send_telegram_notification_url
from main.models import Booking, TelegramChat, Contact


def send_to_telegram_chat(text, link):
    for item in TelegramChat.objects.filter(is_active=True):
        send_telegram_notification_url(text, item.chat_id, link)


def prepare_and_send_booking_to_telegram(request, booking: Booking):
    link = request.build_absolute_uri(
        reverse('admin:main_booking_change', args=(booking.id,))
    )
    text = f'Новый заказ! \n\n'
    send_to_telegram_chat(text, link)


def prepare_and_send_contact_to_telegram(request, contact: Contact):
    link = request.build_absolute_uri(
        reverse('admin:main_contact_change', args=(contact.id,))
    )
    text = f'Новыя заявка! \n\n'
    send_to_telegram_chat(text, link)
