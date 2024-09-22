from django.shortcuts import render
from .models import package,Destinations,Book
from math import ceil
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    b_data=package.objects.all()
    p=Paginator(b_data,2)
    pn=request.GET.get('page')
    f=p.get_page(pn)
    if request.method=="GET":
        st=request.GET.get('ip')
        if st!=None:
            b_data=package.objects.filter(package_name__icontains=st)    
    dis={'packeg':b_data,'f':f}
    return render (request,'Home.html',dis)

def about(request):
    return render (request,'About.html')

def book(request):                            
    return render (request,'Book.html')
def Package(request):
    desti=Destinations.objects.all()
    print(desti)
    desti_dis={'d':desti}
    return render (request,'Package.html',desti_dis)

def submet(request):
        if request.method == "POST":
            name = request.POST.get('name',''),
            email = request.POST.get('email','')
            phone = request.POST.get('phone','')
            address = request.POST.get('address','')
            location = request.POST.get('location','')
            arrivals = request.POST.get('arrivals','')
            leaving = request.POST.get('leaving','')
            guests = request.POST.get('guests','')
            print(name)
            book=Book(name=name,email=email,phone=phone,address=address,location=location,arrivals=arrivals,leaving=leaving,guests=guests)
            book.save()
        return render (request,'Book.html')
    
def Packagedet(request,myid):    
    packagee=package.objects.get(id=myid)
    data={'pc':packagee}
    return render (request,'packebook.html',data)
    
