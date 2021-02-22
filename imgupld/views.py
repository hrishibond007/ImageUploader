from django.shortcuts import render,HttpResponse
from .userForm import ImageForm
from .models import Image

# Create your views here.

def home(request):
    if request.method == "POST":
        print(request)
        form = ImageForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
    form = ImageForm()
    IMG = Image.objects.all()
    print(IMG)
    return render(request,"imgupld/home.html",{"IMG" : IMG,"form" : form})
    
  
