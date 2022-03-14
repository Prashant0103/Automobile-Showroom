from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from auto.models import Customer, car
from django.shortcuts import redirect, render
from django.contrib import auth,messages
from auto.forms import cform,uform,cont


@login_required(login_url='/')
def index(request):
    return render(request,"index.html")


@login_required(login_url='/')
def about(request):
    return render(request,'about.html')


@login_required(login_url='/')
class dropdown:
    @login_required(login_url='/')
    def d_all(request):
        try:
            data = car.objects.all()
            return render(request,'search.html',{'data':data})
        except:
            return redirect('/index')
        
    @login_required(login_url='/')
    def d_Coupe(request):
        try:
            data = car.objects.all().filter(type='Coupe')
            return render(request,'search.html',{'data':data})
        except: 
            return redirect('/index')
    
    @login_required(login_url='/')  
    def d_Hatchback(request):
        try:
            data = car.objects.all().filter(type='Hatchback')
            return render(request,'search.html',{'data':data})
        except:
            return redirect('/index')

    @login_required(login_url='/')
    def d_Sedan(request):
        try:
            data = car.objects.all().filter(type='Sedan')
            return redirect(request,'search.html',{'data':data})
        except:
            return redirect('/index')

    @login_required(login_url='/')
    def d_SUV(request):
        try:
            data = car.objects.all().filter(type='SUV')
            return render(request,'search.html',{'data':data})
        except:
            return redirect('/index')
        
    @login_required(login_url='/')
    def d_Sports(request):
        try:
            data = car.objects.all().filter(type='Sports')
            return render(request,'search.html',{'data':data})
        except:
            return redirect('/index')
    
    @login_required(login_url='/')
    def d_Supercar(request):
        try:
            data = car.objects.all().filter(type='Supercar')
            return render(request,'search.html',{'data':data})
        except:
            return redirect('/index')
    
    @login_required(login_url='/')
    def d_Van(request):
        try:
            data = car.objects.all().filter(type='VAN')
            return render(request,'search.html',{'data':data})
        except:
            return redirect('/index')
    
    
@login_required(login_url='/')
def contact(request):
    if request.method=="POST":
            form = cont()
            if request.method == 'POST':
                form = cont(request.POST)
                if form.is_valid():
                    user = form.save()
                    user.save()
                    profile = form.save(commit=False)
                    profile.user = user            
                    profile.save()
                    name = form.cleaned_data['name']
                    registered = True
                    line = f"Thank You {name}, Your message send Successfully"
                    messages.success(request,line)
                    return redirect('/contact')
                else:
                    messages.error(request,'something went wrong...')
    else:
        form = cont()
        return render(request,'contact.html',{'fm':form})
    

@login_required(login_url='/')
def ulogout(request):
    logout(request)
    messages.success(request,'Your Logout Succesfully...')
    return redirect('/')

    
def register(request):
    if request.method=="POST":
            form = uform()
            if request.method == 'POST':
                form = uform(request.POST)
                if form.is_valid():
                    usern = form.cleaned_data['username']
                    email = form.cleaned_data['email']
                    if Customer.objects.filter(username=usern).first():
                        messages.error(request,'Username Exist Please Choose Different One..')
                        return redirect('/register/')
                    
                    elif Customer.objects.filter(email=email).first():
                        messages.error(request,'Email Exist Plz Login To continue')
                        return redirect('/register/')
                    
                    else:
                        user = form.save()
                        user.save()
                        profile = form.save(commit=False)
                        profile.user = user            
                        profile.save()
                        name = form.cleaned_data['Name']
                        print(name)
                        registered = True
                        messages.success(request,'Your Reg Successfully')
                        return redirect('/')
                else:
                    messages.error(request,'Something Went Wrong')
                    return redirect('register/')
        
    else:
        form = uform()
        return render(request,'register.html',{'form':form})
      


def loginn(request):
    return render(request,"login.html")
  
  
def check_user(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        
        user = authenticate(username=uname,password=passw)
        if user:
            login(request,user)
            messages.success(request,'Your Login Successfully')
            return redirect('/index')
        else:
            messages.error(request,'plz enter valid username and password')
            return render(request,'login.html')
    else:
        messages.error(request,'error')
        return render(request,'login.html')
    
    
@login_required(login_url='/')
def Search(request):
    if request.method == 'POST':
        nm = request.POST.get('fdata')
        data = car.objects.all().filter(name=nm)
        return render(request,'Search.html',{'data':data})
    else:
        return redirect('/index')


    



