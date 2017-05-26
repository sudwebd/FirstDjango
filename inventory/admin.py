from django.contrib import admin

# Register your models here.
from .models import Item
#pass-firstdjango
class ItemAdmin(admin.ModelAdmin):
    list_display=['title','amount']

admin.site.register(Item,ItemAdmin)
