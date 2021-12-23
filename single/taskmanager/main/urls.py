from django.urls import path
from . import views
urlpatterns = [
    path('<int:tp_sort>', views.index),
    path('<str:type_sort>/<int:tp_sort>', views.index_sort, name='sort')
]