import datetime

from django import template
register = template.Library()

    
@register.filter(name='print_timestamp')
def print_timestamp(timestamp):
    """Converts Unix timestamp to a datetime object.
    """
    try:
        ts = int(timestamp)
    except ValueError:
        return None
    return datetime.datetime.fromtimestamp(ts)


@register.filter(name='print_lateness')
def print_lateness(value):
    """Converts a lateness value in seconds to minutes.
    """
    if value == '0':
        return ''
    return str(int(value)/60) + " min"
