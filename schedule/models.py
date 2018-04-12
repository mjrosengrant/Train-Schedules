# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Departure(models.Model):
	NORTH_STATION = "north_station"
	SOUTH_STATION = "south_station"
	ORIGIN_CHOICES = (
		(NORTH_STATION, 'North Station',),
		(SOUTH_STATION, 'South Station',)
	)
	
	DESTINATION_CHOICES = ()

	ON_TIME = 'on_time'
	NOW_BOARDING = 'now_boarding'
	ALL_ABOARD = 'all_aboard'
	DELAYED = 'delayed'
	CANCELLED = 'cancelled'
	INFO_TO_FOLLOW = 'info_to_follow'
	TBD = 'tbd'
	LATE = 'late'
	ARRIVING = 'arriving'
	ARRIVED = 'arrived'
	DEPARTED = 'departed'
	HOLD = 'hold'
	END = 'end'
	STATUS_CHOICES = [
		(ON_TIME, 'On Time',),
		(NOW_BOARDING, 'Now Boarding',),
		(ALL_ABOARD, 'All Aboard',),
		(DELAYED, 'Delayed',),
		(CANCELLED, 'Cancelled',),
		(INFO_TO_FOLLOW, 'Info to follow',),
		(TBD, 'TBD',),
		(LATE, 'Late',),
		(ARRIVING, 'Arriving',),
		(ARRIVED, 'Arrived',),
		(DEPARTED, 'Departed',),
		(HOLD, 'Hold',),
		(END, 'End'),
	]

	timestamp = models.DateTimeField(null=False, blank=False)
	origin = models.CharField(choices=ORIGIN_CHOICES, max_length=64)
	trip = models.IntegerField(null=True, blank=True)
	destination = models.CharField(choices=DESTINATION_CHOICES, max_length=64)
	scheduled_time = models.DateTimeField()
	lateness = models.IntegerField(null=True, blank=True)
	track = models.IntegerField(null=True, blank=True)
	status = models.CharField(choices=STATUS_CHOICES, max_length=64)
