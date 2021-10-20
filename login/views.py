from django.shortcuts import render

# Create your views here.
def index(request, template="login.html"):
    return render(request, template)