from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def profile(request):
    return render(request,'profile.html')

def hobby(request):
    return render(request,'hobby.html')

def suin(request):
    return render(request,"suin.html")

def alcohol(request):
    return render(request,"alcohol.html")