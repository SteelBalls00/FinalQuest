from django_filters import FilterSet, CharFilter, DateFilter
from django import forms
from .models import Announcement

class AnnouncementFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains', label='По заголовку')
    time_create = DateFilter(field_name='time_create', lookup_expr='gt', widget=forms.DateInput(attrs={'type': 'date'}),
                             label='Позже чем')

    class Meta:
        model = Announcement
        fields = ['title', 'time_create']