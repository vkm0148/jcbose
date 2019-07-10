from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Profile


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
# def profile(request):
# 	form = ProfileForm(request.POST or None)
# 	text = ''
# 	if form.is_valid():
# 		post = p_form.save(commit=False)
# 		post.user = request.user
# 		post.save()
# 		# text = p_form.cleaned_data['post']
# 		# p_form = ProfileForm(None)

# 	else:
# 		return render(request, 'profile.html', {'form' : form, 'text' : text})

class profile(TemplateView):
	template_name = 'profile.html'

	def get(self, request, *args, **kwargs):
		current_user = request.user
		if current_user.is_authenticated:
			# If current user if student
			if UserIdPassword.objects.get(user=current_user).token == 0:
				# collecting context data to be passed to template html file
				form_object=ProfileForm.objects.get(Email_id=current_user)
				# context data collected is stored in params dict
				params = {
					'form' : form_object,		}
				# render template with collected context data
				return render(request, self.template_name, params)
			else:
				return redirect('login')
		else:
			return redirect('login')
