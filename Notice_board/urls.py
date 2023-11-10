from django.urls import path
from . import views


urlpatterns = [
    path('', views.AnnouncementsViev.as_view()),
    path("<int:pk>/", views.AnnouncementsDetailViev.as_view())
]