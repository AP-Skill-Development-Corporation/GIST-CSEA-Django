from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sample(self):
	return HttpResponse("Good Evening")

def demo(t,k):
	return HttpResponse("Hi Welcome {}".format(k))

def func(t,a,b):
	return HttpResponse("Hi welcome {1} Your age is {0}".format(a,b))

def ht(self):
	return HttpResponse("<h1>Good Afternoon</h1>")

def test(self):
	return HttpResponse("<h2>Welcome</h2>")

def abc(self,k):
	return HttpResponse("<h1>welcome <span style='color:red'>{}</span></h1>".format(k))

def jst(self,sname):
	return HttpResponse("<script>alert('Hi Welcome {}')</script>".format(sname))

def htm(self):
	return HttpResponse("<html><head><title>Example</title></head><body><h2>Sample Example on Html File</h2></body></html>")

def gy(self):
	return render(self,'demo.html')

def qwt(self,y):
	return render(self,'hy/sample.html',{'g':y})

def ay(s,j,ag):
	return render(s,'hy/qw.html',{'z':j,'c':ag})

def ky(self):
	return render(self,'hy/sq.html')

def de(self):
	if self.method == "POST":
		a = self.POST['un']
		b = self.POST['pd']
		c = self.POST['em']
		return render(self,'hy/disp.html',{'user':a,'mn':c})
	return render(self,'hy/reg.html')




























