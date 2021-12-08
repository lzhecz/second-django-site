from django import template
from django.db.models import Count, F
from django.core.cache import cache

from news.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories(a1='hello', a2='world'):
    categories = Category.objects.annotate(cnt=Count('news', filter = F('news__is_published'))).filter(cnt__gt=0)
    return {'categories': categories, 'a1': a1, 'a2': a2}
