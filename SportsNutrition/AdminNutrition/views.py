from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from SportsNutrition.NutritionStore.forms import RegistrationForm

def admin_page(request):
    return render(request, 'admin_page.html')

def admin_get_user(request):
    users = User.objects.all()
    return render(request, 'admin_user.html', {'users': users})

def admin_del_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/admin/users/')

def admin_get_users(request, user_id):
    print (request.is_ajax())
    if request.is_ajax():
        user = get_object_or_404(User, id=user_id)
        user_form = RegistrationForm(instance=user)
        context = {'form': user_form, 'id': user_id}
        context.update(csrf(request))
        html = loader.render_to_string('inc_reg_form.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404