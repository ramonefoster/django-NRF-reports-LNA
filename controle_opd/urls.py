from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.IndexView.as_view(), name="index"),
    path("dispositivo/<slug:slug>", view=views.SingleAddr.as_view(), name="single-addr")
]
