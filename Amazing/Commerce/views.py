
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from Commerce.models import category,Commerce







    
def index(request):
    Commerce = Commerce.objects.filter(is_sold=False)[0:6]
    category = category.obejects.all()
    return render(request,"index.html",{
        'category ' :category,
        'Commerce' : Commerce
    })
    
   
    
def base(request):
    return render(request,"base.html")


def contact(request):
    return render(request,"contact.html")

def detail(request,pk):
    Commerce = get_object_or_404(Commerce,pk=pk)
    return render(request,'Commerce/detail.html',{
        "Commerce":Commerce
    })

def Signup(request):
    form = SignupForm()

    return render(request,"Commerce/Signup.html",{
        form:"form"
    })