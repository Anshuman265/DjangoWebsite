from django.shortcuts import render

# Create your views here. 
def home(request): 
    return render(request, "home/pages/home.html") 

def chatBot(request):  
    return render(request, "home/pages/chat.html") 

def pressReleases(request): 
    return render(request, "home/pages/pressRelease.html") 
