# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView

from schedule.utils import DepartureAPIWrapper

class DepartureView(TemplateView):
    """Displays the Departure Boards for North and South Station.
    """
    template_name = "schedule/departures.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DepartureView, self).get_context_data(*args, **kwargs)
        api_wrapper = DepartureAPIWrapper()
        station_departures = api_wrapper.get_station_departures()
        context['north_station_departures'] = station_departures['North Station']
        context['south_station_departures'] = station_departures['South Station']
        context['timestamp'] = station_departures["North Station"][1]["TimeStamp"]
        return context

def departure_api_view(request):
    """Get data from MBTA Website."""
    api_wrapper = DepartureAPIWrapper()
    data = api_wrapper.get_station_departures()
    return HttpResponse(data)
