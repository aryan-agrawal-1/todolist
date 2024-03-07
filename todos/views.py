from django.shortcuts import render, redirect, get_object_or_404 # To redirect user
from django.contrib.auth.models import User, auth # Importing user database
from django.contrib import messages # For error messages
from .models import Todos
# Create your views here.

def index(request):
    return render(request, 'index.html')

def todos(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST['name']
            desc = request.POST['desc']
            priority = request.POST['priority']
            date = request.POST['date']

            newTodo = Todos(name=name, desc=desc, priority=priority, date=date, person= request.user)
            newTodo.save()
            messages.success(request, "Todo added!")
        todolist = Todos.objects.filter(person= request.user).filter(isDone = False)
        return render(request, 'todos.html', {'todolist': todolist})
    else:
        return redirect('/')

def delete(request, id):
    todo = get_object_or_404(Todos, id=id)
    todo.delete()
    return redirect('todos')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('todos')
        else:
            messages.info(request, "User does not exist")
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already registered")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already in use")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save;
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')
    else:
        return render(request, 'register.html')
    
def logout(request):
    auth.logout(request)
    return redirect('login')

def profile(request):
    return render(request, 'profile.html')