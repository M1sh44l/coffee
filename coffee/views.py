from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .forms import SignUpForm, SignInForm, CoffeeBeanForm
from .models import CoffeeBean
from django.core.urlresolvers import reverse_lazy

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


def coffeebean_list(request):
	pass

def create_bean(request):
	bean = CoffeeBeanForm(request.POST or None)
	if bean.is_valid():
		bean_object = bean.save()
		bean_object.save()
		return redirect("coffee:list")
	return render(request, "create_bean.html", {"bean": bean})

def update_bean(request):
	bean = CoffeeBeanForm(request.POST or None)
	if bean.is_valid():
		bean_object = bean.save()
		bean_object.save()
		return redirect("coffee:list")
	return render(request, "update_bean.html", {"bean": bean})	


def coffee_list(request):
	object_list = CoffeeBean.objects.all()
	return render(request, "coffee_list.html", {"object_list": object_list})
