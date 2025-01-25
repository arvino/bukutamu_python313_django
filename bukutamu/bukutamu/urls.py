from django.contrib import admin
from django.urls import path
from tamu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.daftar_tamu, name='daftar_tamu'),
    path('tambah/', views.tambah_tamu, name='tambah_tamu'),
] 