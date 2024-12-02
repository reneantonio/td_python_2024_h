from django.shortcuts import render
from .models import Hotel

def listar_hoteles(request):
    hoteles = Hotel.objects.all()
    return render(request,'hoteles.html',{'hoteles':hoteles})
