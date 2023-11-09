from django.urls import path
from . import views


urlpatterns = [
    path('', views.AnnouncementsViev.as_view()),
]