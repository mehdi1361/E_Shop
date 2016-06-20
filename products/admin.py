from django.contrib import admin
from .models import Category, Product, Condition
# Register your models here.
@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "slug", "created_time"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name", "pub_date", "parent"]
