from django.urls import path

from users.views import user_role_detail, user_role_list

urlpatterns = [
    path('user_role_list/', user_role_list, name='user-role-list'),
    path('user_role/<int:pk>/', user_role_detail, name='user-role-detail'),
    # path('user_role/create/', '', name='user-role-create'),
    # path('user_role/update/<int:pk>/', '', name='user-role-update'),
    # path('user_role/delete/<int:pk>/', '', name='user-role-delete')
]
