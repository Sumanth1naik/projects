from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.
def home(requests):
    value1 = questions.objects.all()
    context={
        "q":value1

    }
    return render(requests,'q.html',context)