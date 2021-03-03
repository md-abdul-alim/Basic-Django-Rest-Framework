from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


class UserList(generics.ListCreateAPIView):
    """
    https://www.django-rest-framework.org/api-guide/generic-views/
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

# For more complex cases you might also want to override various methods on the view class.


class UserListCustom(generics.ListCreateAPIView):
    """
    queryset - The queryset that should be used for returning objects from this view.
    Typically, you must either set this attribute, or override the get_queryset() method.
    If you are overriding a view method, it is important that you call get_queryset() instead of accessing this property directly, as queryset will get evaluated once, and those results will be cached for all subsequent requests.
    serializer_class - The serializer class that should be used for validating and deserializing input, and for serializing output. Typically, you must either set this attribute, or override the get_serializer_class() method.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
