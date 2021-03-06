from django.shortcuts import render
from django.conf import settings

# Create your views here.

def home(request):
    context = {}
    
    context['BASE_DIR']     = settings.BASE_DIR 
    context['PROJECT_DIR']  = settings.PROJECT_DIR 
    context['DEBUG']         = settings.DEBUG 
    context['ALLOWED_HOSTS'] = settings.ALLOWED_HOSTS

    return render(request, template_name="home/home_page.html", context=context)