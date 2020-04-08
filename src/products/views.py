from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# no templates
home_text = "Willkommen daheim"
def home_view(request,*args,**kwargs):
    #return HttpResponse(f"<h1>{home_text}</h1>")
    return render(request,"home.html",{})

info_text = "Ich bin Max und lerne gerne. Aber manchmal fehlt mir die Motivation."
def info_view(request,*args,**kwargs):
    #return HttpResponse(f"")
    return render(request,"about.html",{})
philosophy_text = "Meine geistig-moralischen Mechanismen sind mysteriös und komplex."

def philosophy_view(request,*args,**kwargs):
    #return HttpResponse(f"<h3>{philosophy_text}</h3>")
    return render(request,"philosophy.html",{})