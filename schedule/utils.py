"""Utility tools for the Schedule app."""
import csv
import io
import json
import requests
from operator import itemgetter


class DepartureAPIWrapper(object):
    """Accesses Departure CSV from MBTA and translates it into a JSON API."""

    URL = "http://developer.mbta.com/lib/gtrtfs/Departures.csv"
    NORTH_STATION = "North Station"
    SOUTH_STATION = "South Station"

    TIMESTAMP = "TimeStamp"
    ORIGIN = "Origin"
    TRIP = "Trip"
    DESTINATION = "Destination"
    SCHEDULEDTIME = "ScheduledTime"
    LATENESS = "Lateness"
    TRACK = "Track"
    STATUS = "Status"

    def get_station_departures(self):
        """Return all departures organized by the Origin."""
        departures_csv = self._retrieve_csv()
        departures_json = json.loads(self._csv_to_json(departures_csv))

        api_output = {
            self.NORTH_STATION: [],
            self.SOUTH_STATION: []
        }

        # Organize departures by their origin.
        for departure in departures_json:
            api_output[departure[self.ORIGIN]].append(departure)

        # Sort data by scheduled time
        api_output[self.NORTH_STATION] = sorted(
            api_output[self.NORTH_STATION],
            key=itemgetter(self.SCHEDULEDTIME)
        )
        api_output[self.SOUTH_STATION] = sorted(
            api_output[self.SOUTH_STATION],
            key=itemgetter(self.SCHEDULEDTIME)
        )
        return api_output

    def _retrieve_csv(self):
        """Handle request to MBTA for up to date departure information."""
        response = requests.get(self.URL)
        return response.content

    def _csv_to_json(self, departures_csv):
        """Convert csv into more usable json format."""
        reader = csv.DictReader(io.StringIO(unicode(departures_csv)))
        json_data = json.dumps(list(reader))
        return json_data
