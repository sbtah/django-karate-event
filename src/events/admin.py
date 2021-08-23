from django.contrib import admin
from .models import Event, Location

# admin.site.register(Event)
# admin.site.register(Location)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number')
    ordering = ('name',)  # this comma is needed!
    search_fields = ('name', 'address')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'location'), 'event_date',
              'description', 'manager', 'attendees')
    list_display = ('name', 'event_date', 'location', 'manager')
    list_filter = ('event_date', 'location')
    ordering = ('-event_date',)
