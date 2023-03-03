from django.shortcuts import render,redirect
from .models import Student 
# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def register(request):
	q = Student.objects.all()
	if request.method == "POST":
		h = request.POST['a']
		w = request.POST['b']
		z = request.POST['c']
		n = Student(usname=h,pwd=w,email=z)
		n.save()
		return redirect('/reg')
	return render(request,'html/register.html',{'u':q})

def stupd(request,k):
	z = Student.objects.get(id=k)
	if request.method == "POST":
		g = request.POST['usn']
		b = request.POST['stpw']
		p = request.POST['stem']
		z.usname = g
		z.pwd = b
		z.email = p
		z.save()
		return redirect('/reg')
	return render(request,'html/stupdate.html',{'y':z})


