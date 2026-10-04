import uuid

from django.db import models

class Skill(models.Model):
    def __str__(self):
        return self.name

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=True
    )
    date_add = models.DateTimeField(
        auto_now_add=True,
    )
    name = models.CharField(max_length=500)

    class Meta:
        db_table = 'skills'


class Vacancy(models.Model):
    def __str__(self):
        return  f"{self.name} {self.date_published}"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=True
    )
    date_add = models.DateTimeField(
        auto_now_add=True,
    )
    date_published = models.DateTimeField()
    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    URL = models.URLField()

    skills = models.ManyToManyField(
        Skill,
        related_name='vacancies',
        db_table='vacancies_skills_map',
        blank=True,
    )

    class Meta:
        db_table = 'vacancies'

