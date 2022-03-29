from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView


def my_regestration(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    data = {'form':form}
    return render(request, 'register.html', data)

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
def mylogin(request):
    if request.method == 'GET':
        form = AuthenticationForm()
    elif request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('add')
        else:
            return HttpResponse('<h2>Wrong Credentials</h2>')
    data = {'form':form}
    return render(request, 'login.html', data)


def mylogout(request):
    logout(request)
    return redirect('login')

def add(request):
    form = BookForm()
    if request.method=="POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')

    data = {"form":form}
    return render(request,'add.html',data)

def list(request):
    books = Books.objects.all()
    return render(request,'list.html',{"books":books})


class Delete(DeleteView):
    model = Books
    success_url = reverse_lazy('list')
    template_name='books_confirm_delete.html'


class Update(UpdateView):
    model = Books
    form_class = BookForm
    success_url=reverse_lazy('list')
    template_name='books_form.html'
