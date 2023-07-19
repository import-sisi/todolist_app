from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Task)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'priority', 'due_date', 'completed', 'category', 'created_at', 'tag')
    


