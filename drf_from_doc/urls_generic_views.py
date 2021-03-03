from django.urls import path
from . import views_generic_views
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer
urlpatterns = [
    path('userlist/', views_generic_views.UserList.as_view()),
    # OR. same thing we can do it in one line
    path('users/', generics.ListCreateAPIView.as_view(queryset=User.objects.all(),
                                                      serializer_class=UserSerializer), name='user-list'),
    path('userlistcustom/', views_generic_views.UserListCustom.as_view()),
]
