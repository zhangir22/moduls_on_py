from django.db import models
from django import forms


class DataBox(models.Model):
    Date = models.DateField('Дата', max_length=200),
    Name = models.CharField('Название', max_length=200),
    Count = models.IntegerField('Количество'),
    Distance = models.IntegerField('Дистанция'),

    def __str__(self):
        return self.Name


class Meta:
    db_name = 'databox'


class DataBoxForm(forms.ModelForm):
    class Meta:
        model = DataBox
        fields = '__all__'