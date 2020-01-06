from django.shortcuts import render,redirect
from news.models import NewCategory,News
from news.forms import NewsForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='signin')
def home(request):
    form = NewsForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('list')

    context = {
        'a':NewCategory.objects.all(),
        'form':form
    }
    return render(request,'index.html',context)

def list(request):
    a = News.objects.all()
    context = {
        'x':a
    }
    return render(request,'news.html',context)

def edit(request,id):
    x = News.objects.get(pk=id)
    form = NewsForm(request.POST or None,request.FILES or None,instance=x)
    if form.is_valid():
        form.save()
        return redirect('list')
    context = {
        'form':form
    }
    return render(request,'edit.html',context)

def remove(request,id):
    x = News.objects.get(id=id)
    x.delete()
    return redirect('list')

def signin(request):
    if request.method=='POST':
       u = request.POST.get('username')
       p = request.POST.get('password')
       user = authenticate(username=u,password=p)
       if user is not None:
           login(request,user)
           return redirect('home')

    else:
        return render(request,'login.html')


def signout(request):
    logout(request)
    return redirect('signin')

