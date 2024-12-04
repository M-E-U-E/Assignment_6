import json
from django.core.management.base import BaseCommand
from properties.models import Location


class Command(BaseCommand):
    help = "Generate a sitemap.json for all country locations."

    def handle(self, *args, **kwargs):
        try:
            # Query all locations
            locations = Location.objects.order_by("title")

            # Organize locations into a nested structure
            sitemap = []
            countries = locations.filter(location_type="Country")  # Filter only countries
            for country in countries:
                country_data = {
                    "title": country.title,
                    "country_code": country.country_code.lower(),
                    "locations": []
                }

                # Fetch child locations (e.g., states/cities) for this country
                child_locations = locations.filter(parent_id=country.id).order_by("title")
                for child in child_locations:
                    child_data = {
                        "title": child.title,
                        "url": f"{country.country_code.lower()}/{child.title.lower().replace(' ', '-')}"
                    }
                    country_data["locations"].append(child_data)

                sitemap.append(country_data)

            # Write the sitemap to a JSON file
            output_file = "sitemap.json"
            with open(output_file, "w") as sitemap_file:
                json.dump(sitemap, sitemap_file, indent=2)

            self.stdout.write(self.style.SUCCESS("sitemap.json generated successfully!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error generating sitemap: {str(e)}"))
