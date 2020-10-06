from django.shortcuts import render,redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages

# Create your views here.
def home(request):
	#Extracting all values from db
	all_members=Member.objects.all
	return render(request,'home.html',{'all':all_members})

def join(request):
	if request.method=='POST':
		form  = MemberForm(request.POST or None)
		if form.is_valid():
			form.save()
		else:
			fname = request.POST['fname']
			lname = request.POST['lname']
			age = request.POST['age']
			email = request.POST['email']
			passwd = request.POST['passwd']
			messages.success(request,('There was an error in the form'))
			return render(request,'join.html',
				{
					'fname':fname,
					'lname':lname,
					'age':age,
					'email':email,
					'passwd':passwd
				})


		messages.success(request,('Form submitted successfully!'))
		return redirect('home')
	else:
		return render(request,'join.html',{})
