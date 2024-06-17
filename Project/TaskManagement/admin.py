from django.contrib import admin

from TaskManagement.models import Task
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list = ['title', 'description', 'due_date', 'status']
admin.site.register(Task)