from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .models import *
from Userapp.models import Account
from django.contrib import messages

class About(View):
    def get(self,request):
        r = Region.objects.all()
        s = Servi.objects.all()
        return render(request,"about.html", context={"region":r,"servi":s})


class Blogg(View):
    def get(self,request):
        blog  = Blog.objects.all()
        r = Region.objects.all()
        p = Popular_dic.objects.all()
        return render(request,"blog.html",{"bloglar":blog,"region":r,"popular":p})


class Index(View):
    def get(self,request):
        r = Region.objects.all()
        s = Servi.objects.all()
        user = request.user
        return render(request,"index.html",{"region":r,"servi":s, "user":user})


class Search_page(View):
    def get(self,request):
        return render(request,"searchPage.html")



class Popular(View):
    def get(self,request):
        r = Region.objects.all()
        p = Popular_dic.objects.all()
        return render(request,"populard.html",context={"region":r, "popular":p})


class Add_blog(View):
    def get(self,request):
        return render(request,"blogadd.html")
    def post(self,request):
        try:
            f = request.FILES['file']

            title = request.POST.get('title')
            aderes = request.POST.get('aderes')
            author = Account.objects.get(user=request.user)
            Blog(
                file=f,
                title=title,
                aderes=aderes,
                author=author
            ).save()
            return redirect('blog')
        except:
            return redirect('blog')




class Inforadd(View):
    def get(self,request):
        return render(request,"Inforadd.html")
    def post(self,request):
        try:
            name = request.POST.get('n')
            b = request.POST.get('b')
            file = request.FILES('file')
            Region(
                name=name,
                brief_information=b,
                file=file
            )
        except:
            return redirect("/region/")

class Popuadd(View):
    def get(self,request):
        return render(request,"pupuadd.html")
    def post(self,request):
        try:
            file=request.FILES('file')
            r = request.POST.get('r')
            Popular_dic(
                file=file,
                name=r
            ).save()
        except:
            return redirect("/popular/")


class Servisadd(View):
    def get(self,request):
        return render(request,"serviseadd.html")

    def post(self,request):
        try:
            ful=request.POST.get('ful')
            p=request.POST.get('p')
            a=request.POST.get('a')
            f=request.POST.get('f')
            t=request.POST.get('t')
            i=request.POST.get('i')
            f = request.FILES.get('file')
            Servi(
                    fullname = ful,
                    profession = p,
                    about_me = a,
                    facebook_link = f,
                    twitter_link = t,
                    instagram_link = i,
                    images = f

                ).save()
            return redirect('index')
        except:
            return redirect('index')
class Distin(View):
    def get(self,request,pk):
        region = Region.objects.get(id=pk)
        return render(request,"destination.html",{"regions":region})


# class Delet(View):
#     def delete(self,request,pk):
#         ac = Servi.objects.get(account=request.user)
#         s = Servi.objects.get(id=pk)
#         if ac and s:
#             Servi.objects.get(id=pk).delete()
#             return redirect("blog")
#         return redirect("blog")

def like(request,pk):
    user = request.user
    blog = Blog.objects.get(id=pk)
    current_likes = blog.like
    liked = Like.objects.filter(user=user,blog=blog).count()
    print(liked)
    if not liked:
        liked = Like.objects.create(user=user, blog=blog)
        current_likes = current_likes + 1
    else:
        liked = Like.objects.filter(user=user, blog=blog).delete()
        current_likes = current_likes - 1

    blog.like = current_likes
    blog.save()
    return redirect("blog")


