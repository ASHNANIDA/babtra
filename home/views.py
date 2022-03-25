from django.shortcuts import render
from django.http.response import HttpResponse
from . models import *
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from random import random
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(req):
    return HttpResponse("this is sample page")
@api_view(['GET'])
def msg1():
    msg2="this is demo"
    return Response(msg2)

@api_view(['POST'])
def msg3():
    name= request.data['name']
    email= request.data['email']
    place=request.data['place']
    #obj1=request.data
    obj2=b9ajax(name,email,place)
    obj2.save()
    
def about(req):
    return render(req,'fb.html')
def sample(req):
    try: 
        username=req.POST['name']
        obj2= signup.objects.filter(username=username).exists()
        if obj2== False:
            password=req.POST['password']
            email=req.POST['email']
            # age=req.POST['age']
            # place=req.POST['place']
            # dob=req.POST['dob']
            # print(name,age,place,dob)
            obj1=signup(username=username,email=email,password=password)
            obj1.save()
            return render(req,'sample.html',{'message':'user  registered'})
        else:
            return render(req,'sample.html',{'message':'user already  registered'})

    except Exception as e:
        print(e)
    return render(req,'sample.html')

def fnnew(req):
    if (req.method=='POST'):
        name=req.POST['name']
        document=req.FILES['documentt']
        print (name)
        print (document)
        doc_name=str(random())+document.name
        print(doc_name)
        obj1=new(name=name,document=doc_name)
        obj1.save()
        file_obj=FileSystemStorage()
        file_obj.save(doc_name,document)
    return render(req,'new.html')
def old(req):
    obj1=new.objects.all()
    print(obj1)
    return render(req,'old.html',{
        'message':obj1
    })
def log(req):
     try: 
        user=req.POST['username']
        password=req.POST['password']
        obj3=signup.objects.get(username=user,password=password)
        return render(req,'log.html')
     except Exception as e: print(e)
def login(req):
    return render(req,'login.html')
def  payment(req):
    return render(req,'pay.html')
def ajaxb9(request):
    if (request.method=='POST'):
        name = request.POST['name']
        email = request.POST['email']
        place = request.POST['place']
        obj1=b9ajax(name=name,email=email,place=place)
        obj1.save()
        return JsonResponse({"data":"inserted successfully "})
    return render(request,'ajaxb9.html')
def ecom(req):
    pro1=products()
    pro1.image='images/apple.jpg'
    pro1.name='Apple Juice'
    pro1.desc='Fresh and tasty'
    pro1.price= 10
    
   
    
    product =[pro1]
    return render(req,'ecom.html' ,{'product': product})
def main(req):
    return render(req,'main.html')
def home(req):
    return render(req,'home.html')  