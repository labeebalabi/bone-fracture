from django.shortcuts import render
from django.views.decorators.cache import never_cache
from .forms import ImageForm
from .models import Image
# Create your views here.


@never_cache
def home(request):
 if request.method == "POST":
  form = ImageForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
 form = ImageForm()
 img = Image.objects.last()
 return render(request, 'myapp/home.html', {'img':img, 'form':form})


#vaish.qis@gmail.com