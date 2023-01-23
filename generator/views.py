from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
   return render(request, 'generator/home.html')

def password(request):

   alphabets = list('abcdefghijklmnopqrstuvwxyz')
   if request.GET.get('uppercase'):
      alphabets.extend(list('ABCDEFFGHIJKLMNOPQRSTUVWXYZ'))

   if request.GET.get('numbers'):
      alphabets.extend(list('0123456789'))      

   if request.GET.get('special'):
      alphabets.extend(list('!@#$%^&*():?><'))   

   length =int(request.GET.get('length'))

   thepassword=""

   for x in range(length):
      thepassword+= random.choice(alphabets)

   return render(request, 'generator/password.html', {'password' :thepassword})


def about(request):
   return render(request, 'generator/about.html')   