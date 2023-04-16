from django.contrib import admin
from .models import *

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'done_per_cent', 'date_create']
    

@admin.register(TODO)
class TODOAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'name', 'is_done', 'date_create']
