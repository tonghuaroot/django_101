from django.shortcuts import render
from django.shortcuts import HttpResponse
from fuck import models


def index(request):
    if request.method == 'POST':
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        models.UserInfo.objects.create(user=username,pwd=password)
        user_list = models.UserInfo.objects.all()
    elif request.method == 'GET':
    	user_list = models.UserInfo.objects.all()
    return render(request,"index.html",{"data":user_list})

