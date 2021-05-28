from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from . models import contact


# Create your views here.


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("Hello, world. You're at about.")


def index(request):
    context = {"variable1": "Journey.com",
               "variable2": "SargentX"}
    return render(request, 'index.html', context)
    # return HttpResponse("Hello, world. You're at home.")


def Home(request):
    return render(request, 'Home.html')
    # return HttpResponse("Hello, world. You're at homepage.")


def Contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        Contact = contact(name=name, phone=phone, email=email,
                          desc=desc, date=datetime.today())
        Contact.save()
    return render(request, 'Contact.html')
    # return HttpResponse("Hello, world. You can contact us at +91-9719112913.")
