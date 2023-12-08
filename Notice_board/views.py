from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Announcement, Category, UserProfile, Response
from .filters import AnnouncementFilter

from django.shortcuts import redirect
from .forms import ResponseForm, AnnouncementForm
from allauth.account.models import EmailAddress


class AnnouncementsViev(ListView):
    model = Announcement
    ordering = '-time_create'
    template_name = 'Notice_board/announcement_list.html'
    announcements = Announcement.objects.all()
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AnnouncementFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['filterset'] = self.filterset
        return context

    def auth_check(request):
        user_authenticated = request.user.is_authenticated
        email_not_confirmed = not request.user.email_confirmed if user_authenticated else False

        context = {
            'user_authenticated': user_authenticated,
            'email_not_confirmed': email_not_confirmed,
        }

        return render(request, 'Notice_board/announcement_list.html', context)


class AnnouncementsDetailViev(DetailView):
    model = Announcement
    template_name = 'Notice_board/announcement_detail.html'
    context_object_name = 'announcement_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_url'] = "http://127.0.0.1:8000/media/" + str(self.object.image)
        context['email_not_confirmed'] = not self.request.user.groups.filter(name = 'email_confirmed').exists()
        # context['is_not_author'] = not self.request.user.groups.filter(name = 'authors').exists()

        return context



class CreateResponse(LoginRequiredMixin, CreateView):
        form_class = ResponseForm
        model = Response
        template_name = 'Notice_board/response_create.html'


        def form_valid(self, form):
            response = form.save(commit=False)
            user_profile = UserProfile.objects.get(user=self.request.user)
            response.user = user_profile
            response.announcement_id = self.request.GET.get('announcement_id')
            response.save()
            return super().form_valid(form)



class AnnouncementCreate(CreateView):
    # permission_required = ('announcement.add_announcement')
    form_class = AnnouncementForm
    model = Announcement
    template_name = 'Notice_board/announcement_create.html'
    context_object_name = 'announcement_create'

    def form_valid(self, form):
        announcement = form.save(commit=False)
        user_profile = UserProfile.objects.get(user=self.request.user)
        # user_profile = get_object_or_404(UserProfile, user=self.request.user)
        announcement.user = user_profile

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AnnouncementUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('announcement.update_announcement')
    form_class = AnnouncementForm
    model = Announcement
    template_name = 'Notice_board/announcement_create.html'
    context_object_name = 'announcement_update'
    success_url = reverse_lazy('announcement_detail')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)


class AnnouncementDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('announcement.delete_announcement')
    model = Announcement
    template_name = 'Notice_board/announcement_delete.html'
    context_object_name = 'announcement_delete'
    success_url = reverse_lazy('announcement_list')
