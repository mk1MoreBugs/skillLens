from django.contrib import admin

from .models import Vacancy, Skill

admin.site.register([Vacancy, Skill])
