from django.contrib import admin

from .models import Project, Category, Tag


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'created_time', 'category', 'source', 'demo']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
admin.site.register(Tag)