from django.contrib import admin

from .models import Contributor, Article

admin.site.register(Contributor)
admin.site.register(Article)