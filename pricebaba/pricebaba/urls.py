"""pricebaba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from user_management.views import listings_page,add_edit_users,add_update_user

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', listings_page, name='listings_page'),
    url(r'^add-edit-user/', add_edit_users, name="add_edit_users"),
    url(r'^add-update-user/', add_update_user, name="add_update_user"),
    # url(r'^test/', test_path, name="test_path"),
    # url(r'^edit/(?P<user_id>\d+)/$', edit_user, name="edit_user"),
]
