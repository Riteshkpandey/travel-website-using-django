from django.shortcuts import render
from django.core.mail import send_mail
from tour import settings

# from django.http.response import HttpResponse

# Create your views here.
def home(req):
    return render(req,"homepage.html")
def book_now(req):
    if req.method=="POST":
        Fname=req.POST['firstname']
        mobile_number=req.POST['mobile number']
        to=req.POST['to']
        Date=req.POST['date']
        vehicle=req.POST['Vehicle']
        category=req.POST['category']
        
        str1='Name-'+Fname+"\n"+'Mobile Number-'+mobile_number+"\n"+'Destination-'+to+"\n"+'Date-'+Date+"\n"+'Vehicle-'+vehicle+"\n"+'Category-'+category
        
       
        send_mail(
            'NEW BOOKING',str1,settings.EMAIL_HOST_USER,['rkpdjango@gmail.com'],fail_silently=False)
    
    
    return render(req,"book_now.html")