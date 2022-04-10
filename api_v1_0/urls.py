from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getTask/', views.get_task, name='get_task'),
    path('createTask/', views.create_task, name='createTask'),
    path('editTask/<str:task_id>/', views.edit_task, name='editTask'),
    path('deleteTask/<str:task_id>/', views.delete_task, name='deleteTask'),
]
