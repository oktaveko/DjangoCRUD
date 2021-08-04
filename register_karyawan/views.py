from django.shortcuts import render, redirect
from .forms import FormKaryawan
from .models import Karyawan

# Create your views here.
def daftar_karyawan(request):
    context = {'daftar_karyawan' : Karyawan.objects.all()}
    return render(request, "register_karyawan/daftar_karyawan.html", context)

def form_karyawan(request, id=0):
    if request.method == "GET":
        if id==0:
            form = FormKaryawan()
        else:
            karyawan = Karyawan.objects.get(pk=id)
            form = FormKaryawan(instance=karyawan)
        return render(request, "register_karyawan/form_karyawan.html", {'form':form})
    else:
        if id == 0:
            form = FormKaryawan(request.POST)
        else:
            karyawan = Karyawan.objects.get(pk=id)
            form =FormKaryawan(request.POST,instance=karyawan)
        if form.is_valid():
            form.save()
        return redirect('/karyawan/daftar')

def hapus_karyawan(request, id):
    karyawan = Karyawan.objects.get(pk=id)
    karyawan.delete()
    return redirect('/karyawan/daftar')