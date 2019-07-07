from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home_view(request, *args, **kwargs):
	return render(request, "index.html", {})

def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created successfully for {username}!')
			# return redirect('home')
		else:
			messages.error(request,f"Error creating account")
	else:	
		form = UserCreationForm()
	return render(request, "reg.html", {'form': form})

@login_required
def profile(request):
	return render(request, "profile.html")