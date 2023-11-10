from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Announcement



class AnnouncementsViev(ListView):
    model = Announcement
    template_name = 'announcement_list.html'
    announcements = Announcement.objects.all()

    # def get(self, request):
        # return render(request, 'Notice_board/announcement_list.html', {'announcement_list': announcements})


class AnnouncementsDetailViev(DetailView):
    model = Announcement
    template_name = 'Notice_board/announcement_detail.html'
    context_object_name = 'announcement_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_url'] = "http://127.0.0.1:8000/media/" + str(self.object.image)
        return context