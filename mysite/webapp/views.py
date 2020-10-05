from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post, PostSeries, PostCategory
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.
def single_slug(request,single_slug):
	categories = [c.category_slug for c in PostCategory.objects.all()]
	if single_slug in categories:
		matching_series=PostSeries.objects.filter(post_category__category_slug=single_slug)

		series_urls={}
		for m in matching_series.all():
			part_one=Post.objects.filter(post_series__post_series=m.post_series).earliest('post_published')
			series_urls[m]=part_one.post_slug
		return render(request,"main/category.html",
			{"part_ones":series_urls})

	posts = [p.post_slug for p in Post.objects.all()]
	if single_slug in posts:
		this_post=Post.objects.get(post_slug=single_slug)
		return render(request,"main/post.html",
				{"post":this_post})

	return HttpResponse(f"{single_slug} does not correspond to anything")



def homepage(request):
	return render(request=request,
		template_name="main/categories.html",
		context={"categories":PostCategory.objects.all})

def register(request):
	if request.method == "POST":
		form=NewUserForm(request.POST)
		if form.is_valid():
			user=form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f"New Account Created : {username}")
			login(request,user)
			return redirect("webapp:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request,f"{msg}:{form.error_messages}")
	form=NewUserForm()
	return render(request=request,
					template_name="main/register.html",
					context={"form":form})


def logout_request(request):
	logout(request)
	messages.info(request,"Logged Out Successfully")
	return redirect("webapp:homepage")

def login_request(request):
	if request.method=="POST":
		form=AuthenticationForm(request,data=request.POST)
		if form.is_valid():
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			user=authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				messages.info(request,f"You Are Now Logged In As : {username}")
				return redirect("webapp:homepage")
			else:
				messages.error(request, "Invalid Username or Password")
		else:
			messages.error(request, "Invalid Username or Password")
	form=AuthenticationForm()
	return render(request=request,
					template_name="main/login.html",
					context={"form":form})