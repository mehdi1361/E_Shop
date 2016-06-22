from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50, verbose_name= _('country name'), null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=
