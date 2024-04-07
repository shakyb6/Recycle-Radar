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
    path('uabout/',views.about,name='uabout'),
    path('ucontact/',views.about,name='ucontact'),
    path('service/',views.service,name='service'),
    path('logout/', views.logout_view, name='logout'),
    path('price/', views.price_list, name='price'),
    path('uprice/', views.price_list, name='uprice'),


    path('home/',views.home,name='home'),

    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('ucomplaint/',views.ucomplaint,name='ucomplaint'),
    path('ucomlist/',views.ucomlist,name='ucomlist'),
    path('u_list/',views.u_list,name='u_list'),
    
    path('usprofile/',views.usprofile,name='usprofile'),
    path('usupdate/',views.usupdate,name='usupdate'),
    path('uspro/',views.uspro,name='uspro'),

    path('booknow/',views.booknow,name='booknow'),
    path('mybookings/',views.mybookings,name='mybookings'),
    path('delete/<int:id>',views.delete_booking,name="delete_booking"),
    path('cancel/<int:id>',views.cancel_booking,name="cancel_booking"),



    path('accept_user_booking/<int:owner_id>/<int:booking_id>',views.accept_user_booking, name='accept_user'),
    path('adlogin/',views.adlogin,name='adlogin'),
    path('adhome/',views.adhome,name='adhome'),
    path('adbooking/',views.adminbookings,name='adbooking'),
    path('adcancel/<int:id>',views.ad_cancel_booking,name="cancel_booking"),
    path('addelete/<int:id>',views.ad_delete_booking,name="addelete_booking"),
    path('adpayment/',views.adpayment,name="adpayment"),

    path('payment/<int:id>/', views.payment, name='payment'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),



   
    













    












    
    
]
