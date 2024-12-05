from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Location, Accommodation, LocalizeAccommodation


# Define a resource class for Location
class LocationResource(resources.ModelResource):
    class Meta:
        model = Location
        fields = ('id', 'title', 'location_type', 'country_code', 'state_abbr', 'city')  # Fields for import/export


# Admin class for Location
@admin.register(Location)
class LocationAdmin(ImportExportModelAdmin):
    resource_class = LocationResource
    list_display = ('id', 'title', 'location_type', 'country_code', 'state_abbr', 'city')
    list_filter = ('location_type', 'country_code', 'state_abbr')


# Admin class for Accommodation
@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'country_code', 'bedroom_count', 'review_score', 'usd_rate', 'published')
    list_filter = ('country_code', 'published', 'review_score')


# Admin class for LocalizeAccommodation
@admin.register(LocalizeAccommodation)
class LocalizeAccommodationAdmin(admin.ModelAdmin):
    list_display = ('id', 'property_id', 'language')
    list_filter = ('language',)
