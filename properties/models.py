from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField  # Updated import for JSONField

class Location(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=100)
    center = models.PointField()
    parent_id = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True
    )
    location_type = models.CharField(max_length=20)
    country_code = models.CharField(max_length=2)
    state_abbr = models.CharField(max_length=3)
    city = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Accommodation(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    feed = models.PositiveSmallIntegerField(default=0)
    title = models.CharField(max_length=100)
    country_code = models.CharField(max_length=2)
    bedroom_count = models.PositiveIntegerField()
    review_score = models.DecimalField(max_digits=4, decimal_places=1, default=0.0)
    usd_rate = models.DecimalField(max_digits=10, decimal_places=2)
    center = models.PointField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # Corrected indentation
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class LocalizeAccommodation(models.Model):
    id = models.AutoField(primary_key=True)
    property_id = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    language = models.CharField(max_length=2)
    description = models.TextField()
    policy = JSONField()  # Updated JSONField import

    def __str__(self):
        return f"{self.property_id.title} ({self.language})"

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

class PropertyOwner(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)