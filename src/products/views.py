from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# no templates
home_text = "Willkommen daheim"
info_text = "Ich bin Max und lerne gerne. Aber manchmal fehlt mir die Motivation."
philosophy_text = "Meine geistig-moralischen Mechanismen sind mysteriös und komplex."

def home_view(request,*args,**kwargs):
    #return HttpResponse(f"<h1>{home_text}</h1>")
    return render(request,"home.html",{})


def about_view(request,*args,**kwargs):
    #return HttpResponse(f"")
    my_context={
        "list":[3,1,4,1,5,9,2,6,5,3],
    }
    return render(request,"about.html",my_context)

def philosophy_view(request,*args,**kwargs):
    #return HttpResponse(f"<h3>{philosophy_text}</h3>")
    return render(request,"philosophy.html",{})