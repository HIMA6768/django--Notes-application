from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import notes
from django.contrib.auth.models import User
from django.contrib .auth import authenticate,login,logout
# Create your views here.
def about(req):
    return render(req,'about.html')
def  homepage(req):
    nn= ""
    n=[]
    if req.user.is_authenticated:
        n=notes.objects.filter(user=req.user)
        nn=req.user.username
    return render(req,'index.html',context={'cards':n,"name":nn})

def notesave(req):
    r=req.POST
    t=r.get("title")
    d=r.get("description")
    u=req.user.id
    if u is not None:
     n=notes(name=t,description=d,user_id=u)
     n.save()
     return redirect("/")
    else:
        return render(req,"login.html")

def notedelete(req,id):
    d=notes.objects.get(id=id)
    d.delete()
    return redirect("/")
def noteedit(req,id):
    e=notes.objects.get(id=id)
    return render(req,'editnote.html',context={'data':e})
def updatenote(req,id):
    ud= notes.objects.get(id=id)
    r=req.POST
    ud.name=r.get("title")
    ud.description=r.get("description")
    ud.image=req.FILES.get("image")
    ud.save()
    return redirect("/")
def viewnote(req,id):
    v=notes.objects.get(id=id)
    return render(req,'view.html',context={'view':v})

def signup(req):
    return render(req,"signup.html")

def saveuser(req):
    error=None
    r=req.POST
    username=r.get("username")
    email=r.get("email")
    password=r.get("password1")
    if User.objects.filter(username=username).exists():
            error="username already exist"
            return render(req,"signup.html",{"error":error})

    user = User.objects.create_user(username=username, email=email, password=password)
    login(req,user)
    return redirect("/")

def loginuser(req):
    return render(req,"login.html")

def loginchk(req):
    r= req.POST
    username=r.get("username")
    password=r.get("password")
    user= authenticate(req,username=username,password=password)
    if user is not None:
     login(req,user)
     return redirect("/")
    else:
        error ="invalid credentials"
        return render(req,"login.html",{"error":error})


def logoutuser(req):
    logout(req)
    return redirect("/")



