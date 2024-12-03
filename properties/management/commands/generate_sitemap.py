import json
from django.core.management.base import BaseCommand
from properties.models import Location

class Command(BaseCommand):
    help = "Generate a sitemap.json file for all country locations."

    def handle(self, *args, **kwargs):
        try:
            # Query all country-level locations
            country_locations = Location.objects.filter(location_type="country").values(
                "id", "title", "country_code", "center"
            )

            # Prepare the sitemap data
            sitemap_data = [
                {
                    "id": location["id"],
                    "title": location["title"],
                    "country_code": location["country_code"],
                    "center": {
                        "latitude": location["center"].y,
                        "longitude": location["center"].x,
                    }
                }
                for location in country_locations
            ]

            # Write the sitemap data to a JSON file
            output_file = "sitemap.json"
            with open(output_file, "w") as file:
                json.dump(sitemap_data, file, indent=4)

            self.stdout.write(self.style.SUCCESS(f"Sitemap generated: {output_file}"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error generating sitemap: {str(e)}"))
