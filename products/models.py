from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Condition(models.Model):
    created_time = models.DateTimeField(_('creation time'), auto_now_add=True)
    title = models.CharField(_('title'), max_length=50)
    slug = models.SlugField(_('slug title'), help_text=_('Use ascii characters'))

    class Meta:
        db_table = "conditions"

    def __str__(self):
        return self.title

class Specification(models.Model):
    TYPE_CHOICES = (
        (1, _('type1')),
        (2, _('type2')),
        (3, _('type3')),
    )

    created_time = models.DateTimeField(_('creation time'), auto_now_add=True)
    title = models.CharField(_('title'), max_length=50)
    slug = models.SlugField(_('slug title'), help_text=_('Use ascii characters'))
    description = models.TextField(_('description'), blank=True)
    spec_type = models.PositiveSmallIntegerField(_('spec type'), choices=TYPE_CHOICES, default=1)

    class Meta:
        db_table = "specs"

    def __str__(self):
        return self.title

class SpecificationValue(models.Model):
    created_time = models.DateTimeField(_('creation time'), auto_now_add=True)
    specification = models.ForeignKey(Specification, verbose_name=_('Specification'))
    display_value = models.CharField(_('display value'), max_length=150)
    slug = models.SlugField(_('slug value'), help_text=_('Use ascii characters'), blank=True)
    is_filter_option = models.BooleanField(_("Display for filtering?"), default=False,
                                           help_text=_('If marked this value will be available for search filtering'))



    class Meta:
        db_table = "specs_values"
        ordering = ["specification_id", "id"]

    def __str__(self):
        return '%s - %s' % (self.specification, self.display_value)

class Category(models.Model):
    name = models.CharField(max_lenght=50,  _('category name'))
    pub_date = models.DateTimeField(auto_now_add=True, _('category publish time'))

    class Meta:
        db_table = "category"
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_lenght=50,  _('product name'))
    pub_date = models.DateTimeField(auto_now_add=True,  _('product publish time'))
    created_at = models.DateTimeField(auto_now=True), _('product created time')
    parent = models.ForeignKey("self", null=True, blank=True, related_name="children",
    is_hidden = models.BooleanField(_("is hidden?"), default=False)
    is_container = models.BooleanField(_("can contain products?"), default=False)
    avatar = models.ImageField(_('avatar'), blank=True)
    priority_manual = models.PositiveSmallIntegerField(_('manual priority'), default=0,
                                                       help_text=_('This Priority is set by user manually'))
    priority_auto = models.PositiveIntegerField(_('auto priority'), default=0, editable=False,
                                                help_text=_('This Priority is automatically calculated by system'))

    specifications = models.ManyToManyField(Specification, verbose_name=_('specifications'), through='ProductCategorySpec')
    conditions = models.ManyToManyField(Condition, verbose_name=_('conditions'), blank=True)

    class Meta:
        db_table = "products_categories"
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ["-priority_manual", "-priority_auto", "id"]

    def __str__(self):

        return self.display_tree if self.display_tree else self.title



