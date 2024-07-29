from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.http import Http404
import random
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from App_01.models import Contact, Blog
arr=[]
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "index.html")
def add(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        blog = Blog(title = title, content = content, user=request.user)
        blog.save()
        return redirect("/view")
    return render(request, "add.html")
def about(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "about.html")
def contact(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        age = request.POST.get('age')
        contact = Contact(name=name, email=email, age=age, desc=desc, phone=phone, date=datetime.today())
        contact.save()
        
    return render(request, "contact.html")
def update(request):
    if request.user.is_anonymous:
        return redirect("/login")
    blogs = Blog.objects.all()
    user=request.user
    if request.method == "POST":
        title = request.POST.get("updateblog")
        content = request.POST.get("content")
        if(title=="All"):
            Blog.objects.update(content=content)  
        else:
            Blog.objects.filter(title=title).update(content=content) 
        return redirect("/view")
    return render(request, "update.html",{"blogs": blogs,"user": user,"request": request,})
def delete(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method == "POST":
        title = request.POST.get("deleteblog")
        if title == "All":
            for blog in Blog.objects.all():
               Blog.objects.filter(title=blog.title).delete()
        else:
            Blog.objects.filter(title=title).delete()
        return redirect("/view")
    blogs = Blog.objects.all()
    user = request.user
    context = {
        "blogs": blogs,
        "user": user,
        "request": request,
        "code": "<h1>hello</h1>"
    }
    return render(request, 'delete.html', context)
def loginUser(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            print(f"Attempting login for user: {username}")
            user = authenticate(username=username, password=password)
            if user is not None:
                print("Login successful.")
                login(request, user)
                return redirect("/")    
            else:
                print("Login failed.")
                return render(request, "login.html", {"error": "Invalid username or password."})
        return render(request, 'login.html')
    else:
        return redirect("/")

def viewall(request):
    blogs = Blog.objects.all()
    return render(request,"views.html", {"blogs": blogs})
def logoutUser(request):
    logout(request)
    return redirect("/login")
def _404_(request, exception):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "404.html", status=404)
