from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View
from .models import *

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect("index")


class Signup(View):
    def get(self,request):
        return render(request,"signup.html")
    def post(self,request):
        u = request.POST.get('n')
        e = request.POST.get('e')
        pass1 = request.POST.get('p1')
        pass2 = request.POST.get('p2')
        if User.objects.filter(username=u).exists():
            messages.error(request,"This username exists")
            return redirect("signup")
        elif User.objects.filter(email=e).exists():
            messages.error(request, "There is a user with this email address")
            return redirect("signup")
        else:
            if pass1==pass2:
                user = User.objects.create_user(
                    email=e,
                    username=u,
                    password=pass2
                )
                user.save()
                Account.objects.create(user=user)
                messages.info(request, "Account created succesfully.")
                return redirect("login")
            else:
                messages.error(request, "Password error")
                return redirect("signup")

class Login(View):
    def get(self,request):
        return render(request,"login.html")

    def post(self,request):
        username = request.POST.get("e")
        password = request.POST.get("p")
        remember = request.POST.get('ch')
        if remember is None:
            user = authenticate(request, username=username,password=password)
        else:
            user = authenticate(request, username=username, password=password, remember=remember)

        if user is None:
            context = {"error":"Invalid username or password."}
            return render(request,"login.html",context)
        login(request,user)
        return redirect("index")
