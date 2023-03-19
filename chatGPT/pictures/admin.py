from django.contrib import admin
from pictures.models import Pictures


class PicturesAdmin(admin.ModelAdmin):
    list_display = ('name', 'picture', 'picture_url')
    

admin.site.register(Pictures, PicturesAdmin)
