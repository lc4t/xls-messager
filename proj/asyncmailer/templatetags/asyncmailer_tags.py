"""Templatetags for the asyncmailer app."""
from django import template

register = template.Library()

@register.filter
def dict_key(dic, key):
    return dic[key]
