from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def admin_page(request):
    return render(request, 'admin_page.html')

def admin_get_user(request):
    users = User.objects.all()
    return render(request, 'admin_user.html', {'users': users})


def admin_del_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/admin/users/')