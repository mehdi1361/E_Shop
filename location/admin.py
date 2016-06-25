from django.contrib import admin
from .models import Country, State, City

# Register your models here.

class StateAdminInine(admin.TabularInline):
	model = State

class CityAdminInline(admin.TabularInline):
	model = City

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
	list_display = ["id","name", "slug", "created_time"] 
	list_editable = ("name","slug")
	inlines = [StateAdminInine]

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
	list_display = ["id","name", "slug", "created_time"] 
	list_editable = ("name","slug")
	inlines = [CityAdminInline]

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
	list_display = ["id","name", "slug", "created_time"] 
	list_editable = ("name","slug")
