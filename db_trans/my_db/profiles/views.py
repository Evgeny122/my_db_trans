from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse
from .forms import LoginForm, RegisterForm, ProfilesForm
from django.contrib.auth.models import User
from django.http import Http404

def logout_view(request):
    logout(request)
    return redirect('/')

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user_name = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user:
            login(request, user)
            return redirect('/')
    return render(request, 'profiles/forms.html', {'form':form})

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user_name = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(user_name, email, password)
        user.save()
        return redirect('/')
    return render(request, 'profiles/forms.html', {'form' : form, 'register' : True})

def detail_user(request, pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        raise Http404
    return render(request, 'profiles/detail.html', {'profile' : user})
    

def edit_user(request, pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        raise Http404

    if request.method == "POST":
        form = ProfilesForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.profile = user
            obj.save()
    else:
        form = ProfilesForm()

    return render(request, 'profiles/edit_user.html', {'form' : form, 'profile' : user})

def list_users(request):
    try:
        user = User.objects.all()
    except User.DoesNotExist:
        raise Http404
    return render(request, 'profiles/list_users.html', {'profile' : user})