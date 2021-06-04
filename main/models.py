from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from solo.models import SingletonModel

from main.mixins import ImageMixin


class Region(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return self.title


class Hotel(ImageMixin, models.Model):
    region = models.ForeignKey(
        to=Region, on_delete=models.CASCADE, null=True, verbose_name='Регион',
        related_name='hotel_set',
    )
    title = models.CharField(max_length=255, verbose_name='Название')
    short_description = models.TextField(verbose_name='Краткое описание')
    is_recommended = models.BooleanField(default=False)
    image = models.ImageField(upload_to='image/', verbose_name='Фото')
    description = RichTextUploadingField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Почта')
    subject = models.CharField(max_length=255, verbose_name='Тема сообщения')
    text = models.TextField(verbose_name='Текст')
    is_viewed = models.BooleanField(default=False, verbose_name='Просмотрено')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'Контакт #{self.id}'


class Booking(models.Model):
    region = models.ForeignKey(
        Region, on_delete=models.SET_NULL, null=True, verbose_name='Регион',
    )
    hotel = models.ForeignKey(
        Hotel, on_delete=models.SET_NULL, null=True, verbose_name='Отел',
    )
    name = models.CharField(max_length=255, verbose_name='ФИО')
    enter_date = models.DateField(verbose_name='Дата заезда', null=True)
    leave_date = models.DateField(verbose_name='Дата выезда', null=True)
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    adult = models.PositiveSmallIntegerField(verbose_name='Взрослые')
    child = models.PositiveSmallIntegerField(verbose_name='Дети')
    room = models.PositiveSmallIntegerField(verbose_name='Комнаты')
    is_viewed = models.BooleanField(default=False, verbose_name='Просмотрено')

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'

    def __str__(self):
        return f'Бронирование #{self.id}'


class TelegramChat(models.Model):
    class Meta:
        verbose_name = 'Телеграм Чат'
        verbose_name_plural = 'Телеграм Чат'

    title = models.CharField(verbose_name='Заголовок', max_length=255, )
    chat_id = models.CharField(verbose_name='Чат ID', max_length=100, )
    is_active = models.BooleanField(
        default=True, verbose_name='Активный?', db_index=True,
    )

    def __str__(self):
        return self.title


class AbstractInfoModel(ImageMixin, models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='image/', verbose_name='Фото')
    description = RichTextUploadingField(verbose_name='Описание')

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class AboutUs(SingletonModel, AbstractInfoModel):
    class Meta:
        verbose_name = 'О нас'


class OurContact(SingletonModel, AbstractInfoModel):
    class Meta:
        verbose_name = 'Наши Контакты'
