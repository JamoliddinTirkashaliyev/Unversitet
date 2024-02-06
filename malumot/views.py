from django.shortcuts import render,redirect
from .models import *
from .forms import *

def fanlar(request):
    if request.method == 'POST':
        data = FanForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect('/fan/')

    date={
        "fanlar":Fan.objects.all(),
        'form':FanForm(),
    }
    return render(request,"fanlar.html",date)

def fan_tahrirlash(request, pk):
    if request.method == "POST":
        fan = Fan.objects.get(id=pk)
        fan.nom = request.POST['nom']
        fan.yonalish = Yonalish.objects.get(id=request.POST['yonalish'])
        fan.asosi = request.POST.get('asosi') == 'on'

        fan.save()
        return redirect('/fan/')
    context = {
        'fan': Fan.objects.get(id=pk),
        'yonalishlar': Yonalish.objects.all(),
    }
    return render(request, 'fan_tahrirlash.html', context)


def yonalishlar(request):
    if request.method == 'POST':
        data = YonalishForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect('/yonalish/')
    date={
        "yonalishlar":Yonalish.objects.all(),
        'form':YonalishForm()
    }
    return render(request,"yonalishlar.html",date)

def yonalish_tahrirlash(request, pk):
    if request.method == "POST":
        yonalish = Yonalish.objects.get(id=pk)
        yonalish.nom = request.POST['nom']
        yonalish.aktiv = request.POST.get('aktiv') == 'on'

        yonalish.save()
        return redirect('/yonalish/')
    context = {
        'yonalish': Yonalish.objects.get(id=pk),

    }
    return render(request, 'yonalish_tahrirlasha.html', context)


def ustozlar(request):
    if request.method == 'POST':
        data = UstozForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect('/ustoz/')
    date={
        "ustozlar":Ustoz.objects.all(),
        'form':UstozForm()
    }
    return render(request,"ustozlar.html",date)

def ustoz_tahrirlash(request, pk):
    if request.method == "POST":
        ustoz = Ustoz.objects.get(id=pk)
        ustoz.nom = request.POST['ism']
        ustoz.jins = request.POST['jins']
        ustoz.yosh = request.POST['yosh']
        ustoz.daraja = request.POST['daraja']
        ustoz.fan = Fan.objects.get(id=request.POST['fan'])

        ustoz.save()
        return redirect('/ustoz/')
    context = {
        'ustoz': Ustoz.objects.get(id=pk),
        'fanlar': Fan.objects.all(),

    }
    return render(request, 'ustoz_tahrirlash.html', context)

