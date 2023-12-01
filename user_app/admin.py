from django.contrib import admin
from .models import CustomUser, Code

admin.site.register(CustomUser)
admin.site.register(Code)