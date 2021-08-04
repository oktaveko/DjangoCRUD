from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.form_karyawan, name='tambah_karyawan'),
    path('<int:id>/', views.form_karyawan, name='update_karyawan'),
    path('delete/<int:id>/',views.hapus_karyawan, name ='hapus_karyawan'),
    path('daftar/', views.daftar_karyawan, name = 'daftar_karyawan')
]