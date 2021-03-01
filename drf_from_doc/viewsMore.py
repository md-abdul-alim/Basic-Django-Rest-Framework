from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.decorators import api_view


# https://www.django-rest-framework.org/api-guide/views/#class-based-views
class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

# https://www.django-rest-framework.org/api-guide/views/#api_view


@api_view()  # By default only GET methods will be accepted.
def hello_world(request):
    context = {
        'message': 'Hello Abdul Alim'
    }
    # return Response({"message": "Hello World"})
    return Response(context)


@api_view(['GET', 'POST'])
def hello_world_get_post(request):
    if request.method == 'POST':
        # For checking post method first change request type POST. select form-data and use key="name" & value="milon"
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello Abdul Alim"})
