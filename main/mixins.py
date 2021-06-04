from django.templatetags.static import static
from django.utils.safestring import mark_safe


class ImageMixin:

    def image_tag(self):
        if self.image:
            return mark_safe(
                '<img src={} width="130px" />'.format(self.image.url)
            )
        url = static('img/default.png')
        return mark_safe(f'<img src={url} width="130px" />')

    image_tag.short_description = 'Изображение'
