from django.urls import path
from . import views

urlpatterns = [
    path('', views.public_list, name='public_list'),
    path('register/', views.register, name='register'),
    path('member/', views.member_dashboard, name='member_dashboard'),
    path('submit/', views.submit_entry, name='submit_entry'),
    path('edit/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('profile/', views.profile, name='profile'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
] 