from django.urls import path
from . import views

app_name = 'files'  # Add namespace

urlpatterns = [
    path('', views.file_list, name='file_list'),
    path('upload/', views.file_upload, name='file_upload'),
    path('download/<int:pk>/', views.file_download, name='file_download'),
    path('delete/<int:pk>/', views.file_delete, name='file_delete'),
    path('register/', views.register, name='register'),
]