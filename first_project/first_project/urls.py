from django.contrib import admin
from django.urls import path
from django.urls import include
from first_app import views

urlpatterns = [
    path('',include('first_app.urls')),
    path('admin/', admin.site.urls),
]