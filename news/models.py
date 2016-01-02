from datetime import datetime
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField


# Create your models here.
from filer.fields.image import FilerImageField


class News(models.Model):
    class Meta:
        app_label = 'news'
        verbose_name_plural = 'news'

    title = models.CharField(max_length=70)
    slug = models.CharField(max_length=100, unique=True)
    publication_date = models.DateTimeField(default=datetime.now, blank=True)
    text = HTMLField(configuration='CKEDITOR_MODEL_V1', blank=True)
    image = FilerImageField(blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.title


