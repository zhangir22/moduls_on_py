from django.shortcuts import render
from. import models

sql = models.Sql("python_base")


def get_data_from_db():
    objects = list()
    for item in sql.manual("SELECT*FROM sample", response=True):
        objects.append(models.Sample(item.Date.strftime("%d-%m-%Y"), item.Name, item.Count, item.Distance))
    return objects


def index(request):
    examplars = get_data_from_db()
    return render(request, 'main/index.html', {
        'models': examplars
    })

