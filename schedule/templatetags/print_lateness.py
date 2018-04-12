from django import template
import datetime
register = template.Library()

@register.filter(name='print_lateness')
def print_lateness(value):
    if value == '0':
    	return ''
	return str(int(value)/60) + " min"