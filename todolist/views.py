from django.shortcuts import redirect, render

from todolist.forms import TodoForm
from django.http import HttpResponse
from .models import Todo

# Create your views here.

def home(request):
    todolist = Todo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse("Naa Naa")
    context = {'form':form,'todolist':todolist}
    return render(request,'home.html',context)

def delete(request,pk):
    deletetodo = Todo.objects.filter(id=pk)
    if True:
        deletetodo.delete()
        return redirect('home')
    return render(request,'home.html',{'deletetodo':deletetodo})


