from django.urls import path
from .views import *

urlpatterns = [
  path('',index, name='list'),
  path('update_task/<str:pk>/',updateTask, name='update'),
  path('delete_task/<str:pk>/',deleteTask, name='delete'),
]