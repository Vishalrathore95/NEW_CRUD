from django.shortcuts import render, redirect, get_object_or_404
from .models import Testbook

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        Testbook.objects.create(name=name, email=email, password=password)
        return redirect('create')  
    
    data = Testbook.objects.all()
    return render(request, 'index.html',{'data': data})


def show_data(request):
    data = Testbook.objects.all()
    return render(request, 'index.html',{'data': data})


def update_data(request, id):
    item = get_object_or_404(Testbook, id=id)
    if request.method == 'POST':
        item.name = request.POST['name']
        item.email = request.POST['email']
        item.password = request.POST['password']
        item.save()
        return redirect('create')
    return render(request, 'update.html',{'item':item})


def delete_data(request, id):
    item = get_object_or_404(Testbook, id=id)
    item.delete()
    return redirect('create')
 