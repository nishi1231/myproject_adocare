from django.contrib import admin

from .models import UserProfile
from .models import Doctor

admin.site.register(UserProfile)
admin.site.register(Doctor)
