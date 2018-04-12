from django import template
import datetime
register = template.Library()


def get_datetime_from_timestamp(timestamp):
    """Converts Unix timestamp to a datetime object.
    
    Filters using this function decide the format to return it in.
    """
    try:
        ts = int(timestamp)
    except ValueError:
        return None
    return datetime.datetime.fromtimestamp(ts)
    

@register.filter(name='print_timestamp_time')
def print_timestamp_time(timestamp):
    """Returns the time from a Unix timestamp."""
    dt = get_datetime_from_timestamp(timestamp)
    if not dt:
        return None
    return dt.strftime("%I:%M%p")
    
@register.filter(name='print_timestamp')
def print_timestamp(timestamp):
    return get_datetime_from_timestamp(timestamp)


@register.filter(name='print_lateness')
def print_lateness(value):
    """Converts a lateness value in seconds to minutes.
    """
    if value == '0':
        return ''
    return str(int(value)/60) + " min"
