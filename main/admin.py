from django.contrib import admin
from solo.admin import SingletonModelAdmin

from main.models import (
    Hotel, Contact, Region, Booking, TelegramChat, AboutUs, OurContact,
)


@admin.register(Region)
class AdminRegion(admin.ModelAdmin):
    pass


@admin.register(Hotel)
class AdminHotel(admin.ModelAdmin):
    list_display = ['image_tag', 'title', 'region']
    list_display_links = list_display


@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ['__str__', 'is_viewed']
    readonly_fields = ['is_viewed']

    def change_view(self, request, object_id, form_url='', extra_context=None):
        Contact.objects.filter(id=object_id).update(is_viewed=True)
        return super(AdminContact, self).change_view(request, object_id, form_url, extra_context)


@admin.register(Booking)
class AdminBooking(admin.ModelAdmin):
    list_display = ['__str__', 'is_viewed']
    readonly_fields = ['is_viewed']

    def change_view(self, request, object_id, form_url='', extra_context=None):
        Booking.objects.filter(id=object_id).update(is_viewed=True)
        return super(AdminBooking, self).change_view(request, object_id, form_url, extra_context)


@admin.register(TelegramChat)
class AdminTelegramChat(admin.ModelAdmin):
    list_display = ['__str__', 'chat_id']


admin.site.register(AboutUs, SingletonModelAdmin)
admin.site.register(OurContact, SingletonModelAdmin)
