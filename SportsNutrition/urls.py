"""SportsNutrition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from SportsNutrition.NutritionStore.views import index, login, logout, reg
from SportsNutrition.AdminNutrition.views import admin_page, admin_get_user, admin_del_user, admin_get_users, create_user
urlpatterns = [
    url(r'^admin/$', admin_page),
    url(r'^admin/users/$', admin_get_user),
    url(r'^admin/users/del/(?P<user_id>\d+)$', admin_del_user),
    url(r'^admin/users/get/(?P<user_id>\d+)$', admin_get_users),
    url(r'^admin/users/create/(?P<user_id>\d*)$', create_user),
    url(r'^admin_django/$', admin.site.urls),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^reg/$', reg),
    url(r'^', index),
]
