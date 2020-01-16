from django.contrib import admin

# Listing is what you named the model
from .models import Listing

# tweaking the fields displayed
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published','price','list_date','realtor')
    # to make the fields clickable
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title','description','address','city','state','price')
    list_per_page = 25

# Register your models here.
admin.site.register(Listing, ListingAdmin)
