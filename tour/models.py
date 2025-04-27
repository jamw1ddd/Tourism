from django.db import models
from ckeditor.fields import RichTextField


class Region(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    video = RichTextField(blank=True, null=True)
    description = RichTextField()
    location = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='region_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class City(models.Model):
    #region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='cities')
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    video = RichTextField(blank=True, null=True)
    description = RichTextField()
    location = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='city_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Place(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='places')
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    video = RichTextField(blank=True, null=True)
    description = RichTextField()
    location = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='place_images/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"