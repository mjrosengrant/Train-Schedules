from django.conf.urls import include, url
from schedule import views

urlpatterns = [
	url(r'^', views.DepartureView.as_view(), name="departures"),
]
