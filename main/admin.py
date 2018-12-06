from django.contrib import admin

from main.models import Song, Artist

admin.site.register([Artist, Song])
