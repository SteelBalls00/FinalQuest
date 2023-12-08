from django.urls import path
from .views import IndexView
from . import views


urlpatterns = [
    path('', IndexView.as_view()),
    path('response/<int:pk>/accept', views.accept_reply, name="accept_reply"),
    path('response/<int:pk>/delete', views.delete_reply, name="delete_reply"),
]