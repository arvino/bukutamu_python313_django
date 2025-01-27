from django import template
from django.template.defaultfilters import date as date_filter

register = template.Library()

@register.filter
def time_since(value):
    """
    Returns string representing time since date
    e.g., "2 jam yang lalu", "5 menit yang lalu"
    """
    from django.utils import timezone
    from django.utils.timesince import timesince
    
    now = timezone.now()
    try:
        difference = now - value
    except:
        return value

    if difference.days > 7:
        return date_filter(value, "d M Y H:i")
        
    return f"{timesince(value)} yang lalu"

@register.filter
def truncate_chars(value, max_length):
    """
    Truncates a string after a certain number of characters
    """
    if len(value) > max_length:
        return value[:max_length] + '...'
    return value 