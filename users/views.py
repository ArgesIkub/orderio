from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from users.models import CustomUser, UserRole
from django.urls import reverse

# Create your views here.
def user_role_list(request):
    return render(request, 'users/user_role_list.html', {})

def user_role_detail(request, pk):
    try:
        user_role_obj = UserRole.objects.get(id=pk)
        return render(request, 'users/user_role_detail.html', 
        {'user_role_name': user_role_obj.name})
    except:
        return render(request, 'users/no_records.html', {})

