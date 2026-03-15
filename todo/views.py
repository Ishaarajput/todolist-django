from django.shortcuts import render,redirect
from .models import userreg,Task

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=userreg(username=username,email=email,password=password)
        user.save()
        return render(request,'login.html')
    return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=userreg.objects.filter(username=username,password=password).first()
        if user:
            return render(request,'dashboard.html')
        else:
            return render(request,'login.html')
    return render(request, 'login.html')

def addtask(request):
    if request.method == "POST":
        title=request.POST.get("task")
        Task.objects.create(title=title)
    return redirect("dashboard")


def complete(request,id):

    task = Task.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect("dashboard")


def delete(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("dashboard")
        
def dashboard(request):

    search = request.GET.get("search")

    if search:
        tasks = Task.objects.filter(title__icontains=search)
    else:
        tasks = Task.objects.all()

    return render(request, "dashboard.html", {"tasks": tasks})


    

