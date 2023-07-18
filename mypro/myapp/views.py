from django.shortcuts import render
from myapp.models import *

# Create your views here.
def home(request):
    return render(request,'home.html')

def adddata(request):
    if request.method =='POST':
        User.objects.create(
        firstname = request.POST["firstname"],
        lastname = request.POST["lastname"],
        email = request.POST["email"],
        password= request.POST["password"],
        mobile = request.POST["mobile"],
        gender= request.POST["gender"],
        address= request.POST["address"],
        city = request.POST["city"]
        )
        return render(request,'home.html',{"msg": "Data added successfully"})
    else:

        return render(request,'home.html',{"msg": "invalid access"})
    
def showdata(request):
    alldata=User.objects.all()
    return render(request,'table.html',{"alldata":alldata})

def update(request,pk):
    if request.method=="POST":
     onedata=User.objects.get(id=pk)
     onedata.firstname=request.POST["firstname"]
     onedata.lastname = request.POST["lastname"]
     onedata.email = request.POST["email"]
     onedata.password= request.POST["password"]
     onedata.mobile = request.POST["mobile"]
     onedata.gender= request.POST["gender"]
     onedata.address= request.POST["address"]
     onedata.city = request.POST["city"]
     onedata.save()
     return showdata(request)
    else:
     onedata=User.objects.get(id=pk)
     return render(request,'update.html',{'onedata': onedata})


def delete(request,pk):
    onedata=User.objects.get(id=pk)
    onedata.delete()
    return showdata(request)
    

