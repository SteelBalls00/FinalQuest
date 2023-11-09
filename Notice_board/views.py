from django.shortcuts import render
from django.views.generic.base import View

from .models import Announcement



class AnnouncementsViev(View):

    def get(self, request):
        announcements = Announcement.objects.all()
        return render(request, 'Notice_board/announcement_list.html', {'announcement_list': announcements})
