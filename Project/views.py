from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters import FilterSet

from Notice_board.models import Announcement, Response, UserProfile

def confirm_email_view(request):
    return render(request, 'protect/confirm_email.html')

# class IndexView(LoginRequiredMixin, ListView):
#     model = Announcement
#     template_name = 'protect/index.html'
#     context_object_name = 'replies'
#
#     def get_queryset(self):
#         queryset = Response.objects.filter(userprofile__announcement__author_id=self.request.user.id).order_by('-date')
#         self.filterset = PostFilter(self.request.GET, queryset, request=self.request.user.id)
#         if self.request.GET:
#             return self.filterset.qs
#         return Comment.objects.none()
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filterset'] = self.filterset
#         return context
#
#     def delete_comment(request, comment_id):
#         comment = Comment.objects.get(pk=comment_id)
#         comment.delete()
#         return HttpResponseRedirect('/')
#
#
#     def accept_comment(request, comment_id):
#         comment = Comment.objects.get(pk=comment_id)
#         comment.status = True
#         comment.save()
#         return HttpResponseRedirect('/')