from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team

# Create your views here.
def demo(request):
    return render(request,"index.html")

def demo(request):
    obj=Place.objects.all()
    return render(request,"about.html",{'result':obj})

def demo (request):
    tvj=Team.objects.all()
    return render(request,"about.html",{'teamresult':tvj})


# def demo(request):
#     name="India"
#     return render(request,"homepage.html",{'obj':name})
#     # return  HttpResponse("hello world")

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})

# def about(request):
#     return render(request,"aboutthecompany.html")

# def contact(request):
#     return HttpResponse("Have questions or ready to plan your adventure? Contact Hello Holiday at helloholiday@gmail.com or call +918985789356. We're here to make your travel dreams a reality!")
