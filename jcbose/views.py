from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm

# Create your views here.

def home_view(request, *args, **kwargs):
	return render(request, "index.html", {})

def jcb(request):
	return render(request, "jcbose.html", {})

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
	p_form = ProfileForm(request.POST or None)
	text = ''
	if p_form.is_valid():
		post = p_form.save(commit=False)
		post.user = request.user
		post.save()
		# text = p_form.cleaned_data['post']
		# p_form = ProfileForm(None)

	return render(request, 'profile.html', {'form' : p_form, 'text' : text})
