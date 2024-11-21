from django.contrib import admin
from .models import LogMessage
from .models import Film

admin.site.register(Film)

admin.site.register(LogMessage)
