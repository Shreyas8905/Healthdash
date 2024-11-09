from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


from .forms import CustomAuthenticationForm, CustomUserCreationForm
from .models import usercred


def register(request):
    form= CustomUserCreationForm
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'healthdash/register.html',{'form':form})


def login_view(request):
    form = CustomAuthenticationForm(request, data=request.POST)
    context = {
        'form': form
    }
    if request.method == 'POST':

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inform')


    return render(request, 'healthdash/login.html', context)
@login_required
def inform(request):
    user=request.user
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        guardian = request.POST.get('guardian')
        guardian_phone = request.POST.get('guardian_phone')
        health = request.POST.get('health')
        bloodgroup = request.POST.get('blood-group')
        insurance = request.POST.get('insurance')

        # Here you can create or update the object in the database
        obj = usercred.objects.filter(user=user).first()
        if obj is None:
            usercred.objects.create(
                user=user,
                name=name,
                phone=phone,
                guardian=guardian,
                guardphn=guardian_phone,
                health=health,
                bloodgroup=bloodgroup,
                insurance=insurance
            )

        else:
            obj.name = name
            obj.phone = phone
            obj.guardian = guardian
            obj.guardphn = guardian_phone
            obj.health = health
            obj.bloodgroup = bloodgroup
            obj.insurance = insurance
            obj.save()
            return redirect('login')
    return render(request,'healthdash/credform.html')




