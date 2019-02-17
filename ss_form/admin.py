from django.contrib import admin

# Register your models here.

from .models import UserModule

admin.site.register(UserModule)