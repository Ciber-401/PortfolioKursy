from django.shortcuts import render



def index(request):
    return render(request, "rezume/index.html")

def about(request):
    return render(request, "rezume/about-us.html")

def Skils(request):
    return render(request, "rezume/Skils.html")

