from django.contrib import admin
from .models import Region, City, Place,ContactMessage

admin.site.register(Region)
admin.site.register(City)
admin.site.register(Place)
admin.site.register(ContactMessage)
