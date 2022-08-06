from django.shortcuts import render, HttpResponse
from .models import Speakers
# Create your views here.
def index(request):

   # sp1 = Speakers()
   # sp1.name = 'SPEAKER1'
   # sp1.desc = 'abbcd'
   # sp1.img = 'Speaker 1 pic.jpg'
    
   # sp2 = Speakers()
   # sp2.name = 'SPEAKER2'
   # sp2.desc = 'efffed'
   # sp2.img = 'Speaker 2 pic.jpg'

   # sp3 = Speakers()
   # sp3.name = 'SPEAKER3'
    #sp3.desc = 'ghjggh'
    #sp3.img = 'Speaker 1 pic.jpg'

    #speakers = [sp1,sp2,sp3]  

    speakers = Speakers.objects.all()
    
    return render(request, 'index.html', {'speakers' : speakers})
    #return HttpResponse("This is home page")

def showthis(request):
    
    count= Speakers.objects.all().count()
    
    context= {'count': count}
        
    return render(request, 'index.html', context)















def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about page")

def services(request):
    return HttpResponse("This is services page")

def contact(request):
    return HttpResponse("This is contact page")