from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from .models import userreg, Task

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = userreg(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = userreg.objects.filter(username=username, password=password).first()

        if user:
            request.session['user_id'] = user.id   
            return redirect('dashboard')
        else:
            return redirect('login',{  "error": "Username or Password is incorrect"})

    return render(request, 'login.html')    


def addtask(request):
    if request.method == "POST":
        title = request.POST.get("task")

        user_id = request.session.get('user_id')
        user = userreg.objects.get(id=user_id)

        Task.objects.create(title=title, user=user)

    return redirect("dashboard")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):

    user_id = request.session.get('user_id')

    if not user_id:
        return redirect("login")

    tasks = Task.objects.filter(user_id=user_id)

    return render(request, "dashboard.html", {"tasks": tasks})

def complete(request,id):

    task = Task.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect("dashboard")


def delete(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("dashboard")

def logout(request):
    request.session.flush()
    return redirect("login")
        



    

