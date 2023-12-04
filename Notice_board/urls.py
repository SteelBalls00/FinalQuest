from django.urls import path
from .views import AnnouncementsViev, AnnouncementsDetailViev, create_response, AnnouncementCreate, AnnouncementUpdate, AnnouncementDelete


urlpatterns = [
    path('', AnnouncementsViev.as_view(), name = 'announcement_list'),
    path("<int:pk>/", AnnouncementsDetailViev.as_view(), name = 'announcement_detail'),
    path("reply", create_response, name='reply_to'),
    path("create/", AnnouncementCreate.as_view(), name='create_announcement'),
    path('<int:pk>/update/', AnnouncementUpdate.as_view(), name='announcement_update'),
    path('<int:pk>/delete/', AnnouncementDelete.as_view(), name='announcement_delete'),
]