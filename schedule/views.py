# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
import requests
import datetime
from operator import itemgetter

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView

from schedule.utils import DeparturesAPIHandle


class DepartureView(TemplateView):
    template_name = "schedule/departures.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DepartureView, self).get_context_data(*args, **kwargs)
        # Get data from MBTA Website
        departure_data = self.get_departure_data()
        context['departures'] = departure_data
        # Get update timestamp.
        context['timestamp'] = departure_data[1][0]
        return context

    def get_departure_data(self):
        """Handles request to MBTA for up to date departure information."""
        departures_url = "http://developer.mbta.com/lib/gtrtfs/Departures.csv"
        response = requests.get(departures_url)
        cr = csv.reader(response.content.splitlines(), delimiter=str(','))
        departures_data = list(cr)[1:]
        # Sort departures data by scheduled time.
        return sorted(departures_data, key=itemgetter(4))
