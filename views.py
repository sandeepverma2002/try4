from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    print("test  function is called from view")
    #return HttpResponse("<h1>hello</h1>")
    return render(request,"home.html",{})