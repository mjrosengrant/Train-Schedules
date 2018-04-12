# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView

def get_departure_board(request):
	departures_url = "http://developer.mbta.com/lib/gtrtfs/Departures.csv"
	response = requests.get(departures_url)
	import pdb
	pdb.set_trace()
 
	return HttpResponse("<h1>Departure Board</h1>")
