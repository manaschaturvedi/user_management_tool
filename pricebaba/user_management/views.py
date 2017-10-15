from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Pricebaba_Users
from .forms import AddUpdateForm
import requests


def listings_page(request):
	pricebaba_users = Pricebaba_Users.objects.all()
	data = {'users': pricebaba_users}

	return render(request, 'listings_page.html', data)	


def add_edit_users(request):
	form = AddUpdateForm(request.POST or None)
	data = {'form': form}

	return render(request, 'add_edit_users.html', data)


# def edit_user(request, user_id):
# 	user_data = Pricebaba_Users.objects.get(id=user_id)
# 	first_name = user_data.first_name
# 	last_name = user_data.last_name
# 	email = user_data.email
# 	age = user_data.age
# 	location = user_data.location
# 	mobile = user_data.mobile
# 	dob = user_data.dob
# 	form = AddUpdateForm({'first_name':first_name,'last_name':last_name,'email':email,'age':age,
# 		'location':location,'mobile':mobile,'dob':dob})
# 	data = {'form': form}

# 	return render(request, 'edit_users.html', data)
