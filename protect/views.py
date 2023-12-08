from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from Notice_board.models import Response, Announcement, UserProfile


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'protect/index.html'
    model = Response
    ordering = '-created_at'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['responses'] = Response.objects.filter(user=self.request.user.id).order_by('-created_at')

        return context


# Принять отклик
login_required
def accept_reply(request, pk):
    reply = Response.objects.get(id=pk)
    if reply:
        reply.accepted = True
        reply.save(update_fields=['accepted'])

    return redirect(request.META.get('HTTP_REFERER'))


# Удаляем отклик
@login_required
def delete_reply(request, pk):
    Response.objects.get(id=pk).delete()
    return redirect(request.META.get('HTTP_REFERER'))