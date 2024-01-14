from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,"email taken")
                 return redirect('register')
            else:
                 user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                 user.save();
                 return render(request,"login.html")

        else:
            messages.info(request,"password incorrect")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def form(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,"email taken")
                 return redirect('register')
            else:
                 user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                 user.save();
                 return redirect('login')

        else:
            messages.info(request,"password incorrect")
            return redirect('register')
        return redirect('/')
    return render(request,"dd.html")

def regform(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        dateofbirth = request.POST.get('dateofbirth')
        email = request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        phonenumber=request.POST.get('phonenumber')
        district=request.POST.get('district')
        branch=request.POST.get('branch')
        account=request.POST.get('account')
        accounttype = request.POST.get('accounttype')
        user = User.objects.create_user(firstname=firstname,dateofbirth=dateofbirth,age=age,gender=gender,address=address,
                                        email=email,phonenumber=phonenumber,branch=branch,district=district,account=account,accounttype=accounttype)
        user.save();
        messages.info(request, "Registration  successful!")
        return redirect('/')

    return render(request, "form.html")





def signout(request):

    return redirect('/')


# Create your views here.
