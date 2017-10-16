from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from .models import Pricebaba_Users
from .forms import AddUpdateForm
import requests, datetime, time, re


def listings_page(request):
	pricebaba_users = Pricebaba_Users.objects.all()
	data = {'users': pricebaba_users}

	return render(request, 'listings_page.html', data)	


def add_edit_users(request):
	form = AddUpdateForm(request.POST or None)
	data = {'form': form}

	return render(request, 'add_edit_users.html', data)


def add_update_user(request):
	dob_datetime = datetime.datetime.strptime(str(request.POST.get('dob')), "%m/%d/%Y")
	dob = int(dob_datetime.strftime("%s"))
	message = ''
	if(request.POST.get('new_user').encode('utf8') == 'yes'):
		usr = Pricebaba_Users(first_name=request.POST.get('first_name'),
				last_name=request.POST.get('last_name'),age=request.POST.get('age'),dob=str(dob),
				location=request.POST.get('place'),mobile=request.POST.get('mobile'),
				email=request.POST.get('email'))
		usr.save()
		message = 'new user added'
	else:
		obj, created = Pricebaba_Users.objects.update_or_create(
							    id=request.POST.get('user_id').encode('utf8'),
							    defaults={'first_name':request.POST.get('first_name'),
				'last_name':request.POST.get('last_name'),'age':request.POST.get('age'),'dob':str(dob),
				'location':request.POST.get('place'),'mobile':request.POST.get('mobile'),
				'email':request.POST.get('email')
							   	},
							)
		message = 'existing user updated'

	return JsonResponse({'message':message})


def validate_mobile(request):
	mobile = request.GET.get('mobile', None)
	message = ''
	if(len(mobile) != 10):
		message = 'Please enter a valid 10-digit mobile number'
	elif(re.search('[a-zA-Z]', mobile)):
		message = 'Your mobile number cannot contain letters'
	is_error = 1 if message != '' else 0
	data = {'is_error': is_error}
	if(is_error == 1):
		data['message'] = message
	return JsonResponse(data)