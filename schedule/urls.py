from django.conf.urls import include, url
from schedule import views

urlpatterns = [
	url(r'^departures/', include([
		url(r'^$', views.DepartureView.as_view(), name="departures"),
		url(r'^api/$', views.station_departure_api_view, name="api"),
	]))
]
