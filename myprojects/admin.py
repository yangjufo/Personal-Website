from django.contrib import admin

from .models import Project, Category, Tag


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'demo', 'author']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
admin.site.register(Tag)