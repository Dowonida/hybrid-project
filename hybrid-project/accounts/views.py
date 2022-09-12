from ast import Pass
from multiprocessing import context
from unittest import installHandler
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method =='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
            #비로그인 상태라서 데코레이터를 통해 로그인 창으로 리다이렉트 된 경우
            #로그인한 다음 다시 원래 창으로 되돌아가기 위해서 
        pass
    else:
        form= AuthenticationForm()
    context={
        'form':form

    }
    return render(request, 'accounts/login.html',context)

def logout(request):
    #if request.method == 'POST':
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

def delete(request):#회원탈퇴 
    request.user.delete() #user는 알아서 인식되어있다.
    auth_logout(request)
    return redirect('articles:index')

@login_required #이게 없으면 비로그인 상태에서도 url입력을 통해 write창으로 갈 수가 있다.
def update(request):
    if request.method=='POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context={
        'form':form
    }
    return render(request, 'accounts/update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
        
    else:
        form = PasswordChangeForm(request.user)#임포트 필요
    context={
        'form':form,

    }

    return render(request, 'accounts/change_password.html',context)