from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD
=======
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'HomePage.html')








def contact(request):
    return HttpResponse('contact Page')
>>>>>>> einas
