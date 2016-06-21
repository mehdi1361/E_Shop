from django.contrib import admin
from .models import Category, Product, Condition, Specification, SpecificationValue
# Register your models here.

class SpecificationValueAdmin(admin.TabularInline):
    list_display = ["id","value"]
@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "slug", "created_time"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name", "pub_date", "parent"]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","name", "pub_date", "created_at", "parent", "is_hidden", "is_container", "priority_manual" ]

@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ["id", "created_time", "title", "slug", "description", "spec_type"]


