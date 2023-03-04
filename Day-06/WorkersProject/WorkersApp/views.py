from django.shortcuts import render,redirect
from . forms import Usreg
# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def register(request):
	if request.method == "POST":
		v = Usreg(request.POST)
		if v.is_valid():
			v.save()
			return redirect('/')
	v = Usreg()
	return render(request,'html/register.html',{'g':v})


