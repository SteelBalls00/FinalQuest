from django import forms
from .models import Response, Announcement

class ResponseForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Response
        fields = ['content']


class AnnouncementForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Announcement
        fields = ['category', 'title', 'content', 'image', 'video']