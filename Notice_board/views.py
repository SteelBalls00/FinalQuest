from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Announcement, Category
from .filters import AnnouncementFilter

from django.shortcuts import redirect
from .forms import ResponseForm, AnnouncementForm



class AnnouncementsViev(ListView):
    model = Announcement
    template_name = 'Notice_board/announcement_list.html'
    announcements = Announcement.objects.all()
    paginate_by = 10

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = AnnouncementFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        context['email_not_confirmed'] = not self.request.user.groups.filter(name = 'email_confirmed').exists()
        return context


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


def create_response(requset):
    if requset.method == 'POST':
        form = ResponseForm(requset.POST)
        form.save()
        return HttpResponseRedirect('/')

    form = ResponseForm()


    return render(requset, 'Notice_board/announcement_detail.html', {'form': form})

class AnnouncementCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('announcement.add_announcement')
    form_class = AnnouncementForm
    model = Announcement
    template_name = 'Notice_board/announcement_create.html'
    context_object_name = 'announcement_create'
    success_url = reverse_lazy('announcement_detail')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
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
