from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='list'),
    path('create/', views.task_form, name='create'),
    path('<int:pk>/', views.task_detail, name='detail'),
    path('<int:pk>/update/', views.task_update, name='update'),
    path('<int:pk>/delete/', views.task_delete, name='delete'),
]
