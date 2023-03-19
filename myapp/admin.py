from django.contrib import admin
from .models import Profile, CurrentNews, LiveSession

admin.site.register(Profile)
admin.site.register(CurrentNews)
admin.site.register(LiveSession)