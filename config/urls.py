from django.contrib import admin
from django.urls import path, include
from notes.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('notes/', include('notes.urls')),
    path('tasks/', include('tasks.urls')),
]
