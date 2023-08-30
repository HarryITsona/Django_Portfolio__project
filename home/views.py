from django.shortcuts import render,HttpResponse
from home.models import Contact

def home(request):
    return render(request,'home.html')

def about(request):
    return  render(request,'about.html')

def project(request):
    return  render(request,'project.html')
    
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        ins=Contact(name=name,email=email,message=message)
        ins.save()
        print(name,email,message)
    return  render(request,'contact.html')