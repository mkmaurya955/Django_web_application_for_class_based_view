from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
class GetInput(View):
    def get(self,request):
        return render(request,'getinput.html')
class PostInput(View):
    def get(self,request):
        return render(request,'postinput.html')
class Add(View):
    def get(self,request):
        x=int(request.GET['t1'])
        y=int(request.GET['t2'])
        z=x+y
        return HttpResponse("<html><body bgcolor=blue>Sum is:"+str(z)+"</body></html>")
    def post(self,request):
        x=int(request.POST['t1'])
        y=int(request.POST['t2'])
        z=x+y
        return HttpResponse("<html><body bgcolor=red>Sum is:"+str(z)+"</body></html>")
