import csv, io, json, requests
from operator import itemgetter

class DepartureAPIWrapper(object):
    """Accesses Departures CSV from MBTA website and translates it into a JSON API.
    """
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
        """Returns all departures organized by the Origin"""
        departures_csv = self._retrieve_csv()
        departures_json = json.loads(self._csv_to_json(departures_csv))

        api_output = {
            self.NORTH_STATION: [],
            self.SOUTH_STATION: []
        }

        for departure in departures_json:
            # Organize departures by their origin.
            api_output[departure[self.ORIGIN]].append(departure)

        return api_output
        # Sort data by scheduled time
        sorted_data =  sorted(
            departures_csv,
            key=itemgetter(self.SCHEDULEDTIME)
        )
        return sorted_data


    def _retrieve_csv(self):
        """Handles request to MBTA for up to date departure information."""
        response = requests.get(self.URL)
        return response.content


    def _csv_to_json(self, departures_csv):
        """Converts csv into more usable json format."""
        reader = csv.DictReader(io.StringIO(unicode(departures_csv)))
        json_data = json.dumps(list(reader))
        return json_data


