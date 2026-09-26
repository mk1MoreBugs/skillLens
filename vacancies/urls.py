from django.urls import path

from . import views

urlpatterns = [
    path("index.html", views.vacancy_about_app, name="vacancy-about-app"),
    path("list", views.vacancy_list, name="vacancy-list"),
]
