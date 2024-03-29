"""haritha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),

    path('home/',views.home,name='home'),

    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('ucomplaint/',views.ucomplaint,name='ucomplaint'),
    path('ucomlist/',views.ucomlist,name='ucomlist'),
    path('u_list/',views.u_list,name='u_list'),




    path('usprofile/',views.usprofile,name='usprofile'),
    path('usupdate/',views.usupdate,name='usupdate'),
    path('uspro/',views.uspro,name='uspro'),
 
    path('adlogin/',views.adlogin,name='adlogin'),
    path('adhome/',views.adhome,name='adhome'),

    path('co_reg/',views.co_reg,name='co_reg'),
    path('co_login/',views.co_login,name='co_login'),
    path('co_home/',views.co_home,name='co_home'),
    path('co_profile/',views.co_profile,name='co_profile'),
    path('co_update/',views.co_update,name='co_update'),
    path('co_proupdate/',views.co_proupdate,name='co_proupdate'),

    path('worklist/',views.worklist,name='worklist'),
    path('work/',views.work,name='work'),
    path('aswork/<int:id>',views.aswork,name='aswork'),

    path('complaint/',views.complaint,name='complaint'),
    path('complaintlist/',views.complaintlist,name='complaintlist'),

    path('updatework/',views.updatework,name='updatework'),

    path('w_list/',views.w_list,name='w_list'),
    path('listwork/',views.listwork,name='listwork'),
    path('view/',views.view,name='view'),

    path('listcoordinate/',views.listcoordinate,name='listcoordinate'),
    path('accept_user_booking/<int:id>',views.accept_user_booking, name='accept_user'),
    path('delete/<int:id>',views.delete,name="delete"),

    path('listmember/',views.listmember,name='listmember'),
    path('accept_user_booking1/<int:id>',views.accept_user_booking1, name='accept_user'),
    path('delete1/<int:id>',views.delete1,name="delete"),

    path('listdate/',views.listdate,name='listdate'),
    path('date/',views.date,name='date'),
    path('payment/<int:tool_id>/', views.payment, name='payment'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),



   
    













    












    
    
]
