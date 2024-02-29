from django.shortcuts import render

# Create your views here.
# def index(request):
#     return render(request, "index.html") 

# def register_restaurant(request):
#     return render(request, "register_restaurant.html") 

# def user_register(request):
#     return render(request, "user_register.html") 


from django.shortcuts import render,redirect
from accounts.forms import Userform


# Create your views here.
def index(request):
    return render(request,"index.html")

def registerResturant(request):

    return render(request,"ResturantRegister.html")

def userRegister(request):
    form=Userform()
    return render(request,'userRegister.html',{'form':form})
