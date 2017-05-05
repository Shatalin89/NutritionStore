from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from SportsNutrition.NutritionStore.forms import RegistrationForm
from django.http import Http404, JsonResponse
from django.template import loader
from django.template.context_processors import csrf


def admin_page(request):
    return render(request, 'admin_page.html')

def admin_get_user(request):
    users = User.objects.all()
    form = RegistrationForm
    return render(request, 'admin_user.html', {'users': users, 'form': form})

def admin_del_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/admin/users/')

def admin_get_users(request, user_id):
    if request.is_ajax():
        user = get_object_or_404(User, id=user_id)
        user_form = RegistrationForm(instance=user)
        context = {'form': user_form, 'id': user_id}
        context.update(csrf(request))
        html = loader.render_to_string('inc-admin_edit_users.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404


def create_user(request, user_id=None):
    print(request.is_ajax())
    if request.is_ajax():
        if not user_id:
            user = UserChangeForm(request.POST)
        else:
            user = get_object_or_404(User, id=user_id)
            user = UserChangeForm(request.POST or None, instance=user)
        if user.is_valid():
            user.save()
            users = User.objects.all()
            html = loader.render_to_string('inc_users_list.html', {'users': users}, request=request)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        else:
            errors = user.errors.as_json()
            return JsonResponse({'errors': errors})

    raise Http404