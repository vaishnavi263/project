from django.shortcuts import render
from .models import Course,Contact,Staff
from django.contrib import messages
from django.shortcuts import redirect,render
# Create your views here.
def mainhome(request):
    return render(request,'mainhome.html')

def signup(request):
    if request.method == "POST":
        name =request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phno = request.POST['phno']
        password2 = request.POST['password2']
        if password == password2 :
            if Staff.objects.filter(email = email).exists():
                messages.info(request,'email taken')
                return redirect('signup')
            else:
                customer = Staff.objects.create(email = email,name = name,password = password,phno = phno)
                customer.save()   
                messages.info(request,'user created')
                return redirect('login')
        else:
           messages.info(request,'password is not match')
           return redirect('signup')
    else:
        return render(request,'signup.html')

def signin(request):
    return render(request,"signin.html")  

def forgot(request):
    return render(request,"forgot.html")  



def contact(request):
    if request.method=="POST":
        if request.POST['name'] is not None:
            enq=Contact.objects.create(name=request.POST['name'],email=request.POST['email'],phno=request.POST['phno'])
            enq.save()
            dicts={'out':1,'name':request.POST['name']}
            return render(request,'contact.html',dicts)
        return render(request,'contact.html')   


def course(request):
    courses={
        'course':Course.objects.all()
    }
    return render(request,'course.html',courses)