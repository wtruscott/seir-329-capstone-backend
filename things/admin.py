from django.contrib import admin
from .models import Thing, Container, Place, Collection

# Register your models here.

class ThingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Thing, ThingAdmin)

class CollectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Collection, CollectionAdmin)

class ContainerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Container, ContainerAdmin)

class PlaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Place, PlaceAdmin)