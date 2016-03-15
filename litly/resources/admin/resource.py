from django.contrib import admin
from resources.models import Resource 

@admin.register(Resource)


class ResourceModelAdmin(admin.ModelAdmin):
    
    list_display = admin.ModelAdmin.list_display + (
            'prev_url',
            'next_url',
            )
    



