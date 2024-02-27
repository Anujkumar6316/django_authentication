from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request,'users/index.html')

# Create your views here.
def registration(request):
    if request.method == 'POST':
        reg = UserCreationForm(request.POST)
        if reg.is_valid():
            reg.save()
            return redirect('login')
    else:
        reg=UserCreationForm()
    return render(request, 'users/signup.html',{'form':reg})