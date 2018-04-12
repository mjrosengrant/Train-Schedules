from django import template
import datetime
register = template.Library()

@register.filter(name='print_timestamp')
def print_timestamp(timestamp, time_only=False):
    try:
        ts = int(timestamp)
    except ValueError:
        return None

    dt = datetime.datetime.fromtimestamp(ts)
    if time_only:
        return dt.strftime("%I:%M%p")
    return dt