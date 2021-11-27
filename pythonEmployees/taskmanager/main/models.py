from django.db import models

# Create your models here.

DEPARTMENT_CHOICES = (
     ('Отдел №1', 'Отдел №1'),
     ('Отдел №2', 'Отдел №2'),
     ('Отдел №3', 'Отдел №3'),
     ('Отдел №4', 'Отдел №4'),
     ('Отдел №5', 'Отдел №5'),

)
    #('Отдел №1', 'Отдел №2', 'Отдел №3', 'Отдел №4', 'Отдел №5')
LANGUAGE_CHOICES = (
     ('C#', 'C#'),
     ('Python', 'Python'),
     ('PHP', 'PHP'),
     ('Ruby', 'Ruby'),
     ('C++', 'C++'),

)
    #('C#', 'Python', 'PHP', 'Ruby', 'C++')


class Employee(models.Model):
    name = models.TextField("Имя", max_length=200)
    last_name = models.TextField("Фамилия", max_length=200)
    age = models.IntegerField("Возраст")
    department = models.CharField("Отдел", max_length=100, choices=DEPARTMENT_CHOICES)
    program_language = models.CharField("Язык программирование", max_length=200, choices=LANGUAGE_CHOICES)

    def __str__(self):
        return self.name
