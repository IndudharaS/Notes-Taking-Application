from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('auth/', views.AuthorizedViews.as_view()),
    path('login/',views.LoginInterfaceView.as_view(), name='login'),
    path('signup/',views.SignupView.as_view(),name='signup'),
    # path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    # path('logout-page/', TemplateView.as_view(template_name='logout.html'),
    #      name='logout_page'),
    # path('logout/',views.CustomLogoutView.as_view(), name='logout'),
    path('logout/',views.logout_view, name='logout'),
    path('logged_out/',views.logged_out_view, name='logged_out'),

] 
  