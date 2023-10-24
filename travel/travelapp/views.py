from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import person
from .models import places
#Create your views here.

def index(request):
    obj=places.objects.all()
    object=person.objects.all()
    return render(request, "index.html",{'result':obj,'res':object})

