from django.urls import path
from . import views_generic_views

urlpatterns = [
    path('userlist/', views_generic_views.UserList.as_view()),
    path('userlistcustom/', views_generic_views.UserListCustom.as_view()),
]
