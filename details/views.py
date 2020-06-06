from django.shortcuts import render, redirect
from . models import RouterProperties
from . forms import RouterDataForm


def home(request):
    datas = RouterProperties.objects.all()
    context = {
        'datas':datas
    }
    return render(request, 'home.html', context)


def createdata(request):
    if request.method == 'GET':
        return render(request, 'createdata.html', {'form':RouterDataForm()})
    else:
        try:
            form = RouterDataForm(request.POST)
            form.save()
            return redirect('home')
        except ValueError:
            return render(request, 'createtodo.html', {'form':RouterDataForm(), 'error':'Bad Request'})