from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('events/', views.all_events, name='all-events'),
    path('events/<int:pk>', views.event_details, name='event-details'),
    path('add-location/', views.add_location, name='add-location'),
    path('locations/', views.location_list, name='locations'),
    path('locations/<int:pk>',
         views.location_details, name='location-details'),
    path('locations/search/',
         views.search_locations, name='search-locations'),
]
