from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb
import random as rnd


Con = MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", passwd="", db="sample")
Cursor = Con.cursor()


class DataBoxModel:
    def set_date(self, date):
        self.date = date

    def set_name(self, name):
        self.name = name

    def set_count(self, count):
        self.count = count

    def set_distance(self, distance):
        self.distance = distance

    def get_date(self):
        return self.date

    def get_name(self):
        return self.name

    def get_count(self):
        return self.count

    def get_distance(self):
        return self.distance



def filter(tup):
    lst = []
    for item in tup:
        for i in item:
            lst.append(i)
    return lst


def get_data_from_db(name_column, cursor):
    sql = "SELECT "+name_column+" FROM databox"
    cursor.execute(sql)
    data_list = list()
    for item in cursor:
        data_list.append(item)
    return filter(data_list)


def create_lst_model(dates, names, counts, distances):
    lst_model = []
    count_records = len(dates)
    index = 0
    while index < count_records:
        lst_model.append(DataBoxModel())
        lst_model[index].set_date(dates[index])
        lst_model[index].set_name(names[index])
        lst_model[index].set_count(counts[index])
        lst_model[index].set_distance(distances[index])
        index += 1
    return lst_model


def replace(lst, index):
    lst[index], lst[index+1] = lst[index + 1], lst[index]


def sort_lst(lst, type_sort, tp_sort):
    count = len(lst)
    if type_sort == 'name':
        if tp_sort == 1:
            for i in range(count - 1):
                for j in range(0, count - i - 1):
                    if lst[j].get_name() < lst[j + 1].get_name():
                        replace(lst, j)

        if tp_sort == 0:
            for i in range(count - 1):
                for j in range(0, count - i - 1):
                    if lst[j].get_name() > lst[j + 1].get_name():
                        replace(lst, j)

    if type_sort == 'count':
        if tp_sort == 1:
            for i in range(count - 1):
                for j in range(0, count - i - 1):
                    if lst[j].get_count() < lst[j + 1].get_count():
                        replace(lst, j)

        if tp_sort == 0:
            for i in range(count - 1):
                for j in range(0, count - i - 1):
                    if lst[j].get_count() > lst[j + 1].get_count():
                        replace(lst, j)

    if type_sort == 'distance':
        if tp_sort == 1:
            for i in range(count - 1):
                for j in range(0, count - i - 1):
                    if lst[j].get_distance() > lst[j + 1].get_distance():
                        replace(lst, j)

        if tp_sort == 0:
            for i in range(count - 1):
                for j in range(0, count - i - 1):
                    if lst[j].get_distance() < lst[j + 1].get_distance():
                        replace(lst, j)

    return lst


def get_models(cursor):
    models = create_lst_model(get_data_from_db('Date', cursor),
                              get_data_from_db('Name', cursor),
                              get_data_from_db('Count', cursor),
                              get_data_from_db('Distance', cursor))
    return models


def index_sort(request, type_sort, tp_sort):
    lst_models = sort_lst(lst=get_models(Cursor), type_sort=type_sort, tp_sort=tp_sort)
    return render(request, 'main/index.html', {'models': lst_models, 'tp_sort': tp_sort})


def index(request, tp_sort):
    models = get_models(Cursor)
    rnd.shuffle(models)
    return render(request, 'main/index.html', {
        'models': models, 'tp_sort': tp_sort
    })
