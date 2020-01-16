from django.contrib import admin

# Listing is what you named the model
from .models import Listing

# Register your models here.
admin.site.register(Listing)
