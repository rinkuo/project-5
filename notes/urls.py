from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.note_list, name='list'),
    path('create/', views.note_form, name='create'),
    path('<int:pk>/', views.note_detail, name='detail'),
    path('<int:pk>/update/', views.note_update, name='update'),
    path('<int:pk>/delete/', views.note_delete, name='delete'),
]
