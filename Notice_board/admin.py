from django.contrib import admin
from .models import UserProfile, Category, Announcement, Response


admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Announcement)
admin.site.register(Response)