from django.db import models
from location.models import City
from products.models import Product
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Repository(models.Model):
    TYPE_CHOICES = (
        (1, _('type1')),
        (2, _('type2')),
        (3, _('type3')),
    )
    name = models.CharField(max_length=50,verbose_name=_("repository name"), choices = TYPE_CHOICES)
    city = models.ForeignKey(City,verbose_name=_("city"),related_name='city')
    tel = models.PositiveIntegerField(null=True)
    
    class Meta:
        db_table = "repository"

    def __str__(self):
        return "%s >> %s" % (self.name, self.tel)


class StoreHouse(models.Model):
    repostory = models.ForeignKey(Repository,verbose_name=_("repository"), related_name="repository")
    product = models.ForeignKey(Product,verbose_name=_("product"), related_name="product_store")
    quantity = models.PositiveIntegerField(null=False, default=0)
    
    class Meta:
        db_table = "store_house"

    def __str__(self):
        return "%s >> %s >> %s" % (self.repostory.name,self.repostory.tel, self.product.name)

