from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from core.models import Customer


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        
    return render(request, 'accounts/login.html')


def user_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone_field = request.POST.get('phone_field')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                print("USerName is Already exist .. ")
                return redirect('user_register')            

            else:
                if User.objects.filter(email=email).exists():
                    print("Email is Already exist .. ")
                    return redirect('user_register')
                else:
                    user = User.objects.create_user(
                        username=username, email=email, password=password
                        )
                    user.save()
                    
                    customer_data = Customer(
                        user=user, phone_field=phone_field
                        )
                    customer_data.save()

                    # Code for logging
                    our_user = authenticate(
                        username=username, password=password
                        )
                    if our_user is not None:
                        login(request, user)
                        return redirect('index')
        else:
            return redirect('user_register')            

    return render(request, 'accounts/register.html')


def user_logout(request):
    logout(request)
    return redirect('index')
