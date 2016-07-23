from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
# test for save

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
    name = models.CharField(max_length=50,  verbose_name=_('category name'))
    pub_date = models.DateTimeField(auto_now_add=True,verbose_name= _('category publish time'))
    parent = models.ForeignKey("self", null=True, blank=True, related_name="children")

    class Meta:
        db_table = "category"
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('product name'))
    pub_date = models.DateTimeField(auto_now_add=True,  verbose_name=_('product publish time'))
    created_at = models.DateTimeField(verbose_name=_('product created time'), blank=True, null=True)
    parent = models.ForeignKey("self", null=True, blank=True, related_name="children")
    is_hidden = models.BooleanField(verbose_name=_("is hidden?"), default=False)
    is_container = models.BooleanField(verbose_name=_("can contain products?"), default=False)
#    avatar = models.ImageField(verbose_name=_('avatar'), blank=True)
    priority_manual = models.PositiveSmallIntegerField(verbose_name=_('manual priority'), default=0)
    category = models.ForeignKey(Category, on_delete=None, related_name="cateory", verbose_name=_("category"), default=1)

    class Meta:
        db_table = "products_categories"
        verbose_name = _('Products')
        verbose_name_plural = _('Products')
        ordering = ["id","-created_at"]

    def __str__(self):
       return self.name

class ProductImage(models.Model):
    image = models.ImageField(verbose_name=_('image for product'), null=True)
    # image_url = models.CharField(max_length=200, verbose_name=_('image for product'), null=True)
    pub_date = models.DateTimeField(verbose_name=_('publish_date'), auto_now_add=True)
    description = models.TextField(verbose_name=_('description for image'), null=True, blank=True)
    product= models.ForeignKey(Product,verbose_name=_('product'), related_name='product_image')
    is_enable = models.BooleanField(verbose_name=_('enable for show'), default=False)

    class Meta:
        db_table = "products_images"
        verbose_name = _('ProductsImage')
        verbose_name_plural = _('ProductsImage')
        ordering = ["id","-pub_date"]

    def __str__(self):
       return self.image_url


class ProductPrice(models.Model):
    price = models.PositiveIntegerField(verbose_name=_("price for product"), default=0)
    discount = models.PositiveIntegerField(verbose_name=_("discount for product"), default=0)
    is_enable = models.BooleanField(verbose_name=_("enable?"), default=True)
    product = models.ForeignKey(Product, verbose_name=_("product"), related_name="product_price", default=1)

    class Meta:
        db_table = "product_price_history"
        verbose_name = _("Price History")
        verbose_name_plural = _("Price History")

    def __str__(self):
        return "%s --> %s --> %s" % (self.product.name,self.price, self.discount)







