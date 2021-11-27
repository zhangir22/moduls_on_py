from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('list', views.list_employee, name='page_list'),
    path('add', views.add_employee, name='page_add'),
    path('edit/<str:id>', views.edit_employee, name='page_edit')
]