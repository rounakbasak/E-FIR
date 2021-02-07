from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def indexView(request):
    return render(request,'login-option.html')

def create-policeView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-as-police_url')
    else:
        form = UserCreationForm()
    return render(request,'registration/create-police.html')

def create-userView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-as-user_url')
    else:
        form = UserCreationForm()
    return render(request,'registration/create-police.html')

    return render(request,'registraion/create-user.html')

def loginaspoliceView(request):
    return render(request,'registration/login-as-police.html')

def loginasuserView(request):
    return render(request,'registration/login-as-user.html')

def police-pageView(request):
    return render(request,'police-page.html')

def user-pageView(request):
    return render(request,'user-page.html')


