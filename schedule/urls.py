from django.urls import path

from schedule import views

app_name = 'schedule'
urlpatterns = [
    path(r'^$', views.DepartureView.as_view(), name="departures"),
    path(r'^api/$', views.station_departure_api_view, name="api"),
]
