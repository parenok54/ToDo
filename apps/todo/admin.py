from django.contrib import admin
from apps.todo.models import ToDo

# Register your models here.
@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'is_completed')