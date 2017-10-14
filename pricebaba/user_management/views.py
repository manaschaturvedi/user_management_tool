from django.shortcuts import render, redirect
from .models import Pricebaba_Users
from .forms import AddUpdateForm


def listings_page(request):
	pricebaba_users = Pricebaba_Users.objects.all()
	data = {'users': pricebaba_users}

	return render(request, 'listings_page.html', data)	


def add_edit_users(request):
	form = AddUpdateForm()
	data = {'form': form}

	return render(request, 'add_edit_users.html', data)


