from django.contrib import admin

from .models import Comment, Choice

admin.site.register(Comment)
admin.site.register(Choice)