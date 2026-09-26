from django.http import HttpResponse

from django.shortcuts import render

from .models import Vacancy

def vacancy_about_app(request):
    return HttpResponse("<h1>Vacancies app</h1>")

def vacancy_list(request):
    vacancies =Vacancy.objects.all().order_by("-date_published")
    context = {"vacancies": vacancies}
    return render(
        request,
        template_name="vacancies/list.html",
        context=context,
    )
