from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from .models import Pricebaba_Users
from .forms import AddUpdateForm
import requests, datetime, time, re


def listings_page(request):
	pricebaba_users = Pricebaba_Users.objects.all()
	users_data = []
	for e in pricebaba_users:
		user_dict = {}
		dob_datetime = datetime.datetime.strptime(str(e.dob), "%m/%d/%Y")
		dob = dob_datetime.strftime("%d %B %Y")
		user_dict = {'id':e.id, 'first_name':e.first_name,'last_name':e.last_name,'email':e.email,
				'age':e.age,'dob':dob,'raw_dob':e.dob,'location':e.location,'mobile':e.mobile}
		users_data.append(user_dict)
	data = {'users': users_data}

	return render(request, 'listings_page.html', data)	


def add_edit_users(request):
	form = AddUpdateForm(request.POST or None)
	data = {'form': form}

	return render(request, 'add_edit_users.html', data)


def add_update_user(request):
	dob = request.POST.get('dob');
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
	if(mobile == ''):
		message = 'Your mobile number cannot be blank'
	elif(len(mobile) != 10):
		message = 'Please enter a valid 10-digit mobile number'
	elif(re.search('[a-zA-Z]', mobile)):
		message = 'Your mobile number cannot contain letters'
	is_error = 1 if message != '' else 0
	data = {'is_error': is_error}
	if(is_error == 1):
		data['message'] = message
	return JsonResponse(data)


def validate_first_name(request):
	first_name = request.GET.get('first_name', None)
	message = ''
	if(first_name == ''):
		message = 'First name cannot be blank'
	elif not first_name.isalpha():
		message = 'First name cannot contain numbers, spaces or special characters'
	is_error = 1 if message != '' else 0
	data = {'is_error': is_error}
	if(is_error == 1):
		data['message'] = message
	return JsonResponse(data)


def validate_last_name(request):
	last_name = request.GET.get('last_name', None)
	message = ''
	if(last_name == ''):
		message = 'Last name cannot be blank'
	elif not last_name.isalpha():
		message = 'Last name cannot contain numbers, spaces or special characters'
	is_error = 1 if message != '' else 0
	data = {'is_error': is_error}
	if(is_error == 1):
		data['message'] = message
	return JsonResponse(data)


def validate_email(request):
	email = request.GET.get('email', None)
	message = ''
	if(email == ''):
		message = 'Email cannot be blank'
	is_error = 1 if message != '' else 0
	data = {'is_error': is_error}
	if(is_error == 1):
		data['message'] = message
	return JsonResponse(data)


def validate_age(request):
	age = request.GET.get('age', None)
	message = ''
	if(age == ''):
		message = 'Age cannot be blank'
	is_error = 1 if message != '' else 0
	data = {'is_error': is_error}
	if(is_error == 1):
		data['message'] = message
	return JsonResponse(data)


def validate_dob(request):
	dob = request.GET.get('dob', None)
	message = ''
	if(dob == ''):
		message = 'Date of birth cannot be blank'
	is_error = 1 if message != '' else 0
	data = {'is_error': is_error}
	if(is_error == 1):
		data['message'] = message
	return JsonResponse(data)


def validate_location(request):
	location = request.GET.get('location', None)
	message = ''
	if(location == ''):
		message = 'Location cannot be blank'
	is_error = 1 if message != '' else 0
	data = {'is_error': is_error}
	if(is_error == 1):
		data['message'] = message
	return JsonResponse(data)

