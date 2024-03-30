import random
import email
import smtplib
import razorpay
from django.conf import settings
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.http import Http404
import smtplib
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render,redirect
from .models import reg,coordinate,Assign,feedback,booking,pay,ufeedback
import razorpay #import this
from django.conf import settings
from django.http import JsonResponse #import this
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt #import this
from django.http import HttpResponseBadRequest #import this
from django.contrib.auth import authenticate,login as auth_login,logout

razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

# Create your views here.

def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def service(request):
    return render(request,'service.html')
def home(request):
    return render(request,'home.html')
def staffhome(request):
    return render(request,'staffhome.html')

# user side

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('psw')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        # Check if a user with the provided username or email already exists
        existing_user = User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()
        if existing_user:
            # If a user with the provided username or email already exists, handle accordingly
            # You can redirect the user to a different page or display an error message
            return render(request, "registration_error.html", {"message": "Username or email already exists"})
        else:
            # Create a new user instance and save it to the database
            new_user = User.objects.create_user(username=username, email=email, password=password)
            # Now, create a profile for the new user
            new_profile = reg(username=new_user, email=email, psw=password, phone=phone, address=address)
            new_profile.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        return render(request, "register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('psw')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Authentication successful, log the user in
            auth_login(request, user)
            request.session['profile_id'] = user.profile.id
            return redirect('home')  # Redirect to the homepage after login
        else:
            # Authentication failed, display login page with error message
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        # Display the login page
        return render(request, 'login.html')

@login_required
def usprofile(request):
    try:
        # Get the reg object associated with the current user
        current_user = request.user
        cr = reg.objects.get(username=current_user)

        user_info = {
            'username': cr.username,
            'email': cr.email,
            'psw': cr.psw,
            'address': cr.address,
            'phone': cr.phone,
        }
        return render(request, 'usprofile.html', user_info)
    except reg.DoesNotExist:
        return render(request, 'usprofile.html')


@login_required
def usupdate(request):
    try:
        # Get the reg object associated with the current user
        current_user = request.user
        cr = reg.objects.get(username=current_user)

        user_info = {
            'username': cr.username,
            'email': cr.email,
            'psw': cr.psw,
            'address': cr.address,
            'phone': cr.phone,
        }
        return render(request, 'usupdate.html', user_info)
    except reg.DoesNotExist:
        return render(request, 'usupdate.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import reg

@login_required
def uspro(request):
    try:
        current_user = request.user
        cr = current_user.profile

        if request.method == "POST":
            name = request.POST.get('nametxt')
            email = request.POST.get('emailtxt')
            phone = request.POST.get('phonetxt')
            address = request.POST.get('addresstxt')
            password = request.POST.get('pswtxt')
            
            # Update user information
            cr.email = email
            cr.phone = phone
            cr.address = address
            cr.psw = password  # Assuming psw field is in the reg model
            cr.save()
            return redirect('home')
        else:
            return render(request, 'usupdate.html')
    except reg.DoesNotExist:
        # Handle the case where the user does not exist in the database
        return render(request, 'usupdate.html')








@login_required
def booknow(request):
    if request.method == 'POST':
        user = request.user  # Get the currently logged-in user
        scrap = request.POST.get('scrap')
        quantity = request.POST.get('quantity')
        date = request.POST.get('date')
        location = request.POST.get('location')
        description = request.POST.get('description')

        # Get the reg object associated with the current user
        owner = reg.objects.get(username=user)

        # Create a booking instance for the current user
        booking.objects.create(owner=owner, scrap_name=scrap, scrap_quantity=quantity, date=date, location=location, description=description)
        
        return redirect('home')  # Redirect to the home page after booking
        
    else:
        return render(request, 'booknow.html')

@login_required
def mybookings(request):
    # Get the reg object associated with the current user
    owner = request.user.profile  # Assuming 'profile' is the related name in your OneToOneField
    
    # Filter bookings based on the current user's reg object
    user_bookings = booking.objects.filter(owner=owner)
    
    return render(request, 'mybookings.html', {'data': user_bookings})


def delete_booking(request,id):
    data=booking.objects.get(id=id)
    data.delete()
    return render(request,'home.html')


def adlogin(request):
    if request.method=='POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        u = 'admin'
        p = 'admin'
        if name==u:
            if password==p:
                return render(request,'adhome.html')
            else:
             return render(request,"adlogin.html")
        else:
             return render(request,"adlogin.html")
    else:
         return render(request,"adlogin.html")
    
def adhome(request):
    return render(request,'adhome.html')
 

def co_reg(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        gender=request.POST.get('gender')
        coordinate(fname=fname,lname=lname,email=email,phone=phone,password1=pass1,password2=pass2,gender=gender).save()
        return render(request,'co_login.html')
    else:
        return render(request,'co_reg.html')
    

def co_login(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        # print(name)
        password1 = request.POST.get('password1')
        # print('joy')
        cr = coordinate.objects.filter(fname=fname,password1=password1)
        if cr:
            userd =coordinate.objects.get(fname=fname,password1=password1)
            id=userd.id
            fname=userd.fname
            password1=userd.password1
            request.session['cname']=fname
            return render(request,'co_home.html')
        else:
            
            return render(request,'co_login.html')
    else:
        return render(request,'co_login.html')
    
def co_home(request):
    return render(request,'co_home.html')

def co_profile(request):
    fname=request.session['cname']
    print('name is',fname)
    cr=coordinate.objects.get(fname=fname)
    if cr:
        user_info={
            'fname':cr.fname,
            'lname':cr.lname,
            'email':cr.email,
            'phone':cr.phone,
            'password':cr.password1,
            'gender':cr.gender,
            }
        return render(request,'co_profile.html',user_info)
    else:
        return render(request,'co_profile.html')
    
def co_update(request):
    fname=request.session['cname']
    print('name is',fname)
    cr=coordinate.objects.get(fname=fname)
    if cr:
        user_info={
            'fname':cr.fname,
            'lname':cr.lname,
            'email':cr.email,
            'phone':cr.phone,
            'password':cr.password1,
            'gender':cr.gender,
            }
        return render(request,'co_update.html',user_info)
    else:
        return render(request,'co_update.html')  

def co_proupdate(request):
    fname=request.session['cname']
    if request.method=="POST":
        fname=request.POST.get('fnametxt')
        lname=request.POST.get('lnametxt')
        email=request.POST.get('emailtxt')
        phone=request.POST.get('phonetxt')
        password=request.POST.get('passwordtxt')
        gender=request.POST.get('gendertxt')
        data=coordinate.objects.get(fname=fname)
        data.fname=fname
        data.lname=lname
        data.email=email
        data.phone=phone
        data.password1=password
        data.gender=gender
        data.save()
        return redirect('co_home')
    else:
        return render(request,'co_update.html')
    
def u_list(request):
    data=reg.objects.all()
    return render(request,'u_list.html',{'data':data})



def work(request):
    if request.method=='POST':
        name=request.POST.get('name')
        ward=request.POST.get('ward')
        price=request.POST.get('price')
        date=request.POST.get('date')
        time=request.POST.get('time')
        area=request.POST.get('area')
        description=request.POST.get('description')
        Assign(name=name,ward=ward,price=price,date=date,time=time,area=area,description=description).save()
        return render(request,'co_home.html')
    else:
        return render(request,'work.html',{'name':name,'ward':ward})
    
def aswork(request,id):
    cr=member.objects.get(id=id)
    name=cr.name
    ward=cr.ward
    return render(request,'work.html',{'name':name,'ward':ward})

def ucomplaint(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        ufeedback(name=name,email=email,message=message).save()
        return render(request,'home.html')
    else:
        return render(request,'ucomplaint.html')
def ucomlist(request):
    data=ufeedback.objects.all()
    return render(request,'ucomlist.html',{'data':data})


def worklist(request):
    name=request.session['m_name']
    data = Assign.objects.filter(name=name)
    return render(request,'worklist.html',{'data':data})
    
def complaint(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        feedback(name=name,email=email,message=message).save()
        return render(request,'m_home.html')
    else:
        return render(request,'complaint.html')
    
def complaintlist(request):
    data=feedback.objects.all()
    return render(request,'complaintlist.html',{'data':data})


def w_list(request):
    data=update.objects.all()
    return render(request,'w_list.html',{'data':data})

def listwork(request):
    # fname=request.session['cname']
    data=member.objects.all()
    return render(request,'listwork.html',{'data':data})



def view(request):
    name=request.session['cname']
    data=update.objects.filter(fname=name)
    return render(request,'view.html',{'data':data})






def listcoordinate(request):
    data=coordinate.objects.all()
    return render(request,'listcoordinate.html',{'data':data})

def accept_user_booking(request,id):
    data=coordinate.objects.get(id=id)
    emaill=data.email
    print('email address',emaill)
    print(emaill)
    data.is_accepted = True
    data.save()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("nefsal003@gmail.com", "htxalvzrrkxupspv")
    message = 'You Selected in Post Of HarithaKarmaSena Coordinater'
    s.sendmail("nefsal003@gmail.com",emaill,message)
    s.quit()
    return render(request,'adhome.html')

def delete(request,id):
    data=coordinate.objects.get(id=id)
    data.delete()
    return render(request,'adhome.html')


def listmember(request):
    data=member.objects.all()
    return render(request,'listmember.html',{'data':data})

def accept_user_booking1(request,id):
    data=member.objects.get(id=id)
    emaill=data.email
    print('email address',emaill)
    print(emaill)
    data.is_accepted = True
    data.save()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("nefsal003@gmail.com", "htxalvzrrkxupspv")
    message = 'You Selected in Post Of HarithaKarmaSena Member'
    s.sendmail("nefsal003@gmail.com",emaill,message)
    s.quit()
    return render(request,'adhome.html')

def delete1(request,id):
    data=member.objects.get(id=id)
    data.delete()
    return render(request,'adhome.html')

def listdate(request):
    data=Assign.objects.all()
    return render(request,'listdate.html',{'data':data})


def date(request):
    data=Assign.objects.all()
    return render(request,'date.html',{'data':data})


def payment(request, tool_id=None):
    if tool_id is None:
        # Handle the case where no tool_id is provided
        # Redirect the user to the tool table or show an error message
        return redirect('date')  # Adjust the URL name for your tool table view

    # Get the specific tool using the tool_id
    a = get_object_or_404(Assign, id=tool_id)

    # Rest of your view logic
    amount = int(a.price) * 100  # Convert the product price to cents
    currency = 'INR'
    razorpay_order = razorpay_client.order.create(dict(amount=amount, currency=currency, payment_capture='0'))

    razorpay_order_id = razorpay_order['id']
    callback_url = '/paymenthandler/'

    context = {
        'razorpay_order_id': razorpay_order_id,
        'razorpay_merchant_key': settings.RAZOR_KEY_ID,
        'razorpay_amount': amount,
        'currency': currency,
        'callback_url': callback_url,
    }

    # Create a Payment instance and save it
    try:
        payment_instance = pay(
           
            membername=a.name,
            price=a.price,
  
        )
        payment_instance.save()
    except Exception as e:
        print(f"Error saving payment: {e}")
        

    return render(request, 'payment.html', context=context)

@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                    return render(request, 'pay_success.html')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'pay_failed.html')
            else:
 
                # if signature verification fails.
                return render(request, 'pay_failed.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()
   








            


       