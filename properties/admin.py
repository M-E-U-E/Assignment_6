from django.contrib import admin
from .models import Location, Accommodation, LocalizeAccommodation

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'location_type', 'country_code', 'state_abbr', 'city')
    list_filter = ('location_type', 'country_code', 'state_abbr')


@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'country_code', 'bedroom_count', 'review_score', 'usd_rate', 'published')
    list_filter = ('country_code', 'published', 'review_score')


@admin.register(LocalizeAccommodation)
class LocalizeAccommodationAdmin(admin.ModelAdmin):
    list_display = ('id', 'property_id', 'language')
    list_filter = ('language',)
