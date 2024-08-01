# your_app/templatetags/user_filters.py
from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='is_member_of')
def is_member_of(user, group_name):
    return user.groups.filter(name=group_name).exists()