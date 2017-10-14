from django.shortcuts import render, redirect
from .models import Pricebaba_Users


def listings_page(request):
	pricebaba_users = Pricebaba_Users.objects.all()
	data = {'users': pricebaba_users}

	return render(request, 'listings_page.html', data)	


def add_edit_users(request):
	data = {}

	return render(request, 'add_edit_users.html', data)


