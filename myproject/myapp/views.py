from django.shortcuts import render
from myapp.forms import LogForm

# Create your views here.

def form_view(request):
    form = LogForm()
    context = {"form" : form}
    return render(request, "home.html", context)