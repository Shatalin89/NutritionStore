from django.contrib import auth
from django.shortcuts import render, render_to_response, HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from SportsNutrition.NutritionStore.forms import RegistrationForm

def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        print(request.method)
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            return render(request, 'index.html', {'username': username, 'errors': True})
    raise Http404


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def reg(request):
    print(request.method)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(request, 'reg_form.html', context)
    context = {'form': RegistrationForm()}
    return render(request, 'reg_form.html', context)