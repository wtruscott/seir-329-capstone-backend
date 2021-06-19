from django.contrib import admin

# Register your models here.

class ThingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}