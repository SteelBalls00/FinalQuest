from django.urls import path
from .views import AnnouncementsViev, AnnouncementsDetailViev, CreateResponse, AnnouncementCreate, AnnouncementUpdate, AnnouncementDelete

app_name = 'Notice_board'

urlpatterns = [
    path('', AnnouncementsViev.as_view(), name = 'announcement_list'),
    path("<int:pk>/", AnnouncementsDetailViev.as_view(), name = 'announcement_detail'),
    path("reply/", CreateResponse.as_view(), name='reply_to'),
    path("create/", AnnouncementCreate.as_view(), name='create_announcement'),
    path('<int:pk>/update/', AnnouncementUpdate.as_view(), name='announcement_update'),
    path('<int:pk>/delete/', AnnouncementDelete.as_view(), name='announcement_delete'),
]