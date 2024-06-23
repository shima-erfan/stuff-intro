from django.shortcuts import render
from .models import Stuff
from .utils import paginateStuffs

# Create your views here.
def stuffs(request):
    stuff = Stuff.objects.all()
    custom_range = '' #, stuff = paginateStuffs(request, stuff, 3)
    context = {'stuffs':stuff, 'custom_range':custom_range}
    return render(request, 'stuffs/stuffs.html', context)
