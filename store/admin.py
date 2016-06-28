from django.contrib import admin
# Register your models here.
from .models import CoRepository,StoreHouse

class StoreAdmin(admin.TabularInline):
    model = StoreHouse


@admin.register(CoRepository)
class RepositoryHouseAdmin(admin.ModelAdmin):
   list_display = ["id", "city", "name", "tel", "address"]
   inlines = [StoreAdmin]

