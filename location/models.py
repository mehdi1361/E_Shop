from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
'''
class BaseLocation(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(help_text=_('Use ascii characters'))
    description = models.TextField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_('insert time'))

    class Meat:
        abstract=True

    def __str__(self):
        return self.name
'''

class Country(models.Model):
    #super._meta.get_field('name').verbose_name = 'Whatever'
    #Country._meta.get_field('name').verbose_name = 'Whatever'
    #Country._meta.get_field('name').verbose_name='country name'
    #Country._meta.get_field('slug').verbose_name='country slug'
    #Country._meta.get_field('description').verbose_name='country description'
    name = models.CharField(max_length=50, verbose_name= _('state name'))
    slug = models.SlugField(_('slug state'), help_text=_('Use ascii characters'))
    description = models.TextField(_('description'), blank=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_('insert time'))

    class Meta:
        db_table = "country"
        verbose_name = _('countries')
        verbose_name_plural = _('Countries')
        ordering = ["name"]
    
    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=50, verbose_name= _('state name'))
    slug = models.SlugField(_('slug state'), help_text=_('Use ascii characters'))
    description = models.TextField(_('description'), blank=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_('insert time'))
    country = models.ForeignKey(Country, verbose_name=_('country'), related_name='country', on_delete=None)
    class Meta:
        db_table = "state"
        verbose_name = _('states')
        verbose_name_plural = _('states')
        ordering = ["name"]

    def __str__(self):
        return '%s>%s' % (self.country.name, self.name)

class City(models.Model):
    name = models.CharField(max_length=50, verbose_name= _('city name'))
    slug = models.SlugField(_('slug city'), help_text=_('Use ascii characters'))
    description = models.TextField(_('description'), blank=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_('insert time'))
    state = models.ForeignKey(State, verbose_name=_('state'), related_name='state', on_delete=None)

    class Meta:
        db_table = "city"
        verbose_name = _('cities')
        verbose_name_plural = _('cities')
        ordering = ["name"]

    def __str__(self):
        return '%s>%s>%s' % (self.state.country.name,self.state.name,self.name)


