from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    return render(request,"home.html")
    
def aboutMe(request):
    return render(request,"aboutMe.html")

def portfolioDetails(request):
    return render(request,"portfolio-details.html")

    

