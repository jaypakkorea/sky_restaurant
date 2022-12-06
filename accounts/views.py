from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.http import JsonResponse



def login(request):
    if request.user.is_authenticated:
        return redirect('buk2on_on:index')

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('buk2on_on:index')
    else :

        messages.error(request, 'Please correct the error below.')
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('buk2on_on:index')


def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    print(person.restaurant_set.count())
    if person.restaurant_set.count() >= 10 :
        recentlyUpdate = True
    else :
        recentlyUpdate = False

    context = {
            'person' : person,
            'recentlyUpdate': recentlyUpdate
        }
    return render(request, 'accounts/profile.html',context)


def signup(request):
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST, request.FILES)
        if signup_form.is_valid():
            user = signup_form.save()
            # Profile.objects.create(user=user) #프로필 생성
            auth_login(request, user)
            return redirect('accounts:profile' , user.username )
    
    else:
        signup_form = CustomUserCreationForm()

    context = {
        'signup_form' : signup_form,
    }
    
    return render(request,'accounts/signup.html', context)


def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:profile' , user.username )

    
    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {
        'form' : form,
    }
    
    return render(request,'accounts/update.html', context)


def change_password(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, password_form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:profile' , user.username )
        else :
            messages.error(request, 'Please correct the error below.')

    else:
        password_form = PasswordChangeForm(request.user)

    context = {
        'password_form' : password_form,
    }
    
    return render(request,'accounts/change_password.html', context)


def follow(request, user_pk):
    print('hello')
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
            is_followed = False
        else:
            person.followers.add(request.user)
            is_followed = True
        context = {
            'is_followed' : is_followed,
            'followers_count' : person.followers.count(),
            'followings_count' : person.followings.count(),
        }
        return JsonResponse(context)
    return redirect('accounts:profile', person.username)