from django.shortcuts import render
from .models import UserProfileInfo

def loginview(request):
       x = UserProfileInfo.objects.all()
       return render(request, 'Register/index.html',{'user':x})