from django import template
from django.db.models.aggregates import Count
from ..models import Project, Category, Tag

register = template.Library()


@register.simple_tag
def get_recent_projects(num=5):
    return Project.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Project.objects.dates('created_time', 'year', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_projects=Count('project')).filter(num_projects__gt=0)


@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_projects=Count('project')).filter(num_projects__gt=0)
