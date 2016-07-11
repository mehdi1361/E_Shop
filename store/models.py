from django.db import models
from location.models import City
from products.models import Product
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.

class CoRepository(models.Model):
    city = models.ForeignKey(City,verbose_name=_("city"),related_name='city', default=1)
    name = models.CharField(max_length=50,verbose_name=_("name"),blank=True)
    address = models.CharField(max_length=500,verbose_name=_("address"),blank=True)
    tel = models.PositiveIntegerField(null=True)

    class Meta:
        db_table = "co_repository"
        verbose_name = _("Repository")
        verbose_name_plural = _("Repositories")

    def __str__(self):
        return self.name


class StoreHouse(models.Model):
    repostory = models.ForeignKey(CoRepository, verbose_name = _("repository"), related_name ="repository", default=1)
    product = models.ForeignKey(Product,verbose_name=_("product"), related_name="product_store")
    quantity = models.PositiveIntegerField(null=False, default=0)
    
    class Meta:
        db_table = "store_house"
        verbose_name = _("StoreHouse")
        verbose_name_plural = _("StoreHouses")

    def __str__(self):
        return " %s --> %s --> %s" % (self.repostory.name, self.product.name, self.quantity)


class Factor(models.Model):
    user = models.ForeignKey(User, verbose_name= _("factor user"),default=1)
    created_time = models.DateTimeField(verbose_name=_("created time for factor"), auto_now_add=True)
    is_confirm = models.BooleanField(verbose_name=_("confirm factor"),default=False)
    confirm_time = models.DateTimeField(verbose_name=_("created time for factor"), auto_now=True)
    is_send = models.BooleanField(verbose_name=_("send factor"),default=False)
    send_time = models.DateTimeField(verbose_name=_("send time for factor"), auto_now=True)
    repository = models.ForeignKey(CoRepository, verbose_name=_("factor for repository"),default=1)

    class Meta:
        db_table = "factor"
        verbose_name = _("facror")
        verbose_name_plural = _("facrors")


    def __str__(self):
        return "%s -->%s" % (self.id, self.user)

class ProductFactor(models.Model):
    store = models.ForeignKey(StoreHouse, verbose_name=_("store"), related_name="store")
    factor = models.ForeignKey(Factor, verbose_name = _("factor"),related_name = "factor")
    quantity = models.PositiveIntegerField(null=False, default=0)

    class Meta:
        db_table = "product_factor_history"
        verbose_name = _("product in facror")
        verbose_name_plural = _("products in factor")

    def __str__(self):
        return "%s --> %s" % (self.factor.id,self.store.repostory.name)





























