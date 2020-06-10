from django.contrib import admin
from .models import Category, Creators, Genre, Game, Screansoots, Reviews

importlist = (Category, Creators, Genre, Game, Screansoots, Reviews)
for cl in importlist:
    admin.site.register(cl)

# Register your models here.
