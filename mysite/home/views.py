from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required        1
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

# Create your views here.

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = 'smart/notes'
    
    def get(self,request,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request,*args, **kwargs)

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

# class LogoutInterfaceView(LogoutView):
#     template_name = 'home/logged_out.html'     


# class CustomLogoutView(LogoutView):
#     template_name = 'home/logged_out.html'


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    

# class CustomLogoutView(LogoutView):
#     template_name = 'home/logged_out.html'
    
    
def logout_view(request):
    logout(request)
    return redirect('logged_out')


def logged_out_view(request):
    return render(request, 'home/logged_out.html')

# class AuthorizedViews(LoginRequiredMixin,TemplateView):
#     template_name = 'home/authorized.html'
#     login_url = '/admin'


# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html',{})            1