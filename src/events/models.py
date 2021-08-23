from django.db import models
from application.models import Profile
from application.models import User


class Location(models.Model):

    name = models.CharField('Location Name', max_length=45)
    address = models.CharField(max_length=120)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField('Contact Phone', max_length=25, blank=True)
    web = models.URLField('Website Address', blank=True)
    email_address = models.EmailField("Email Address", blank=True)

    def __str__(self):
        return f"Location: {self.name}"


class Event(models.Model):

    name = models.CharField('Event Name', max_length=35)
    event_date = models.DateTimeField("Event Date")
    location = models.ForeignKey(
        Location, blank=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(Profile, blank=True)

    def __str__(self):
        return f"Event: {self.name},  {self.location}"
