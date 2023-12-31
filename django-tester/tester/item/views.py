from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')
    

def counter(request):
    
    posts =[1,2,3,4,5,6,8,'tim','miles','morales','peter','parker']
    return render(request, 'counter.html' ,{  'posts': posts})


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST ['password']

        user= auth.authenticate(username=username, password=password)

        if user  is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "credentials invalid")
            return redirect('login')

    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already registered')
                return redirect('register')
            elif User.objects.filter(username=username ).exists():
                messages.info(request,'username already used')
                return redirect('register')
            else:
                user = User.objects.create_user(email=email,password=password,username=username)
                user.save()
                return redirect  ('login')
        else:
            messages.info(request, "password incorrect")
            return redirect('register')
        

    else: 
        return render(request,'register.html')
    

def post(request,pk):
    return render(request,'post.html', {' pk':pk} )