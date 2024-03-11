from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import FormView,CreateView,TemplateView,View,UpdateView,DetailView,ListView
from django.urls import reverse
from django.utils import timezone
from django.utils.decorators import method_decorator 
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate,login,logout

from safeapp.models import UserProfile,Safty
from safeapp.form import RegisterForm,LoginForms,UserprofileForm

# from saftyapp.decorators import login_required

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib import messages
from django import forms



decs=[login_required,never_cache]


class SignUpView(CreateView):
    template_name="register.html"
    form_class=RegisterForm

    def get_success_url(self):
        return reverse("signin")

 
class signInView(FormView):
    template_name="login.html"
    form_class=LoginForms

    def post(self,request,*args,**kwargs):
        forms=LoginForms(request.POST)
        if forms.is_valid():
            uname=forms.cleaned_data.get("username")
            pwd=forms.cleaned_data.get("password")
            user_object=authenticate(request,username=uname,password=pwd)

            if user_object:
                login(request,user_object)
                print("successfully.............")
                return redirect("index")
        print("failed")
        messages.error(request,"failed to login invalid credentials")
        return render(request ,"login.html",{"form":forms})

@method_decorator(decs,name="dispatch")
class IndexView(ListView):
    template_name="home.html"
    # form_class=
    model=Safty
    context_object_name="data"

@method_decorator(decs,name="dispatch")
class signoutView(View):
    def get(self,request,*args,**kwargs):
         logout(request)
         return redirect("signin")
    
@method_decorator(decs,name="dispatch")
class ProfileUpdateView(UpdateView):
     template_name='profile_edit.html'
     form_class=UserprofileForm
     model=UserProfile 

     def get_success_url(self):
          return reverse("index")

@method_decorator(decs,name="dispatch")
class ProfileDetailView(DetailView):
     template_name='profile.html'
     model=UserProfile
     context_object_name="data"
     def get_success_url(self):
        return reverse("index")