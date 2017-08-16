from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .forms import SignUpForm, SignInForm

# Create your views here.
def usersignup(request):
	# form = SignUpForm()
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('coffee:userlogin')
	else:
		form = SignUpForm()
	return render(request, "signup.html", {'form': form})

def userlogin(request):
	# form = SignInForm()
	if request.method == 'POST':
		form = SignInForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=raw_password)
			if user is not None:
				login(request, user)
				return redirect("coffee:login")
			else:
				messages.error(request, "Wrong username/password. Pleas try again.")
	else:
		form = SignInForm()
	return render(request, "login.html", {'form': form})

def userlogout(request):
	logout(request)
	return redirect("coffee:login")