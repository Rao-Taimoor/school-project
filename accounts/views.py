from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from .forms  import Userform,Loginform
from django.contrib.auth import login as alogin,authenticate,logout as alogout

from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method=='POST':
        
        email=request.POST['email']
        password=request.POST['password']
        role=request.POST['role']
        try:
            User.objects.get(email=email)
            messages.error(request, "Email is already in use")
            return redirect('signup')
        except User.DoesNotExist:
            user =User.objects.create_user(email=email,password=password,role=role)
            user.set_password(password)
            user.save()
            return redirect('login')
    else:
        
        return render(request,'signup.html',{'form':Userform})


def login(request):
    if request.method == 'POST':
        
        if True:
            email = request.POST['email']
            password = request.POST['password']
            role = request.POST['role']

            # Authenticate user
            user = authenticate(request, email=email, password=password)
            


            if user is not None:
                if role!=user.role:
                    messages.success(request,"input your role correctly")
                    return redirect('login')
                # Log the user in
                
                alogin(request, user)
                return redirect('home')
            else:
                return HttpResponse('Invalid login credentials')
    


    form=Loginform()
    return render(request,'login.html',{'form':Loginform})

def logout(request):
    alogout(request)
    return redirect('login')
    
              

    


            



