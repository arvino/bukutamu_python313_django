from django.shortcuts import render, redirect
from .models import Tamu
from .forms import TamuForm

def daftar_tamu(request):
    tamu_list = Tamu.objects.all().order_by('-tanggal')
    return render(request, 'tamu/daftar_tamu.html', {'tamu_list': tamu_list})

def tambah_tamu(request):
    if request.method == 'POST':
        form = TamuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_tamu')
    else:
        form = TamuForm()
    return render(request, 'tamu/tambah_tamu.html', {'form': form}) 