from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from. models import District,Branch,Account
from .forms import YourForm

# Create your views here.
def AccountType(request):
    account=Account.objects.all()
    return render(request,"district.html")

def allBranches(request,c_slug=None):
    c_page=None
    branches= None
    if c_slug!= None:
        c_page=get_object_or_404(District,slug=c_slug)
        branches=Branch.objects.all().filter(branch=c_page,available=True)

    else:
        branches=Branch.objects.all().filter(available=True)
    return render(request,"district.html",{'district':c_page,'branches':branches})

def BranchDetail(request,c_slug,branch_slug):
    try:
        branch=Branch.objects.get(branch__slug=c_slug,slug=branch_slug)
    except Exception as e:
        raise e
    return render(request,'branch.html',{'branch':branch})
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
                return redirect('register.html')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,"email taken")
                 return redirect('register.html')
            else:
                 user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                 user.save();
                 return render(request,"login.html")

        else:
            messages.info(request,"password incorrect")
            return redirect('register.html')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
def regform(request):
    if request.method == 'POST':
        form = YourForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Form submitted successfully!')

        else:
            messages.error(request, 'Form submission failed. Please check the errors.')
    else:
        form = YourForm()
    return render(request, 'form.html', {'form': form})

def reg(request):
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