# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView

from schedule.utils import DepartureAPIWrapper


class DepartureView(TemplateView):
    """Displays the Departure Boards for North and South Station.
    """
    template_name = "schedule/departures.html"


def station_departure_api_view(request):
    """Get data from MBTA Website."""
    api_wrapper = DepartureAPIWrapper()
    data = api_wrapper.get_station_departures()
    return HttpResponse(json.dumps(data))
