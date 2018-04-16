from django.conf.urls import url

from schedule import views


urlpatterns = [
    url(r'^$', views.DepartureView.as_view(), name="departures"),
    url(r'^api/$', views.station_departure_api_view, name="api"),
]
