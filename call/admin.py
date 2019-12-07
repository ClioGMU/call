from django.contrib import admin

from .models import Post, Country, State

admin.site.register(Post)
admin.site.register(Country)
admin.site.register(State)