from django.contrib.auth.models import User
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view, schema, throttle_classes
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView


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

# https://www.django-rest-framework.org/api-guide/views/#api-policy-decorators

# important: Must read before live work: https://www.django-rest-framework.org/api-guide/throttling/
# important: Must read before live work: https://stackoverflow.com/questions/50255005/django-rest-framework-throttling-per-user-and-per-view
# https://oxpedia.org/wiki/index.php?title=AppSuite:Grizzly#Multiple_Proxies_in_front_of_the_cluster
# https://docs.djangoproject.com/en/3.1/topics/cache/#setting-up-the-cache


class OncePerDayUserThrottle(UserRateThrottle):
    rate = '1/day'


@api_view(['GET'])
@throttle_classes([OncePerDayUserThrottle])
def throttleView(request):
    """
    Limits the rate of API calls that may be made by a given user.

    The user id will be used as a unique cache key if the user is
    authenticated.  For anonymous requests, the IP address of the request will
    be used.
    """
    return Response({'message': 'Processing 1 request per day'})

# same as previous process we can control it from settings


@api_view(['GET'])
def throttleViewSettings(request):
    throttle_classes = [UserRateThrottle]
    return Response({'message': 'Processing 2 request per minute'})

# throttling policy on a per-view or per-viewset basis, using the APIView class-based views.


class ThrottleExampleView(APIView):
    throttle_classes = [UserRateThrottle]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted for ThrottleExampleView'
        }
        return Response(content)
# Or, if you're using the @api_view decorator with function based views.


@api_view(['GET'])
@throttle_classes([UserRateThrottle])
def throttle_example_view(request, format=None):
    content = {
        'status': 'request was permitted throttle_example_view'
    }
    return Response(content)

# View schema decorator
# here schema will also use settings throttling timing


class CustomAutoSchema(AutoSchema):
    def get_link(self, path, method, base_url):
        # override view introspection here...
        pass


@api_view(['GET'])
@schema(CustomAutoSchema())
def viewSchema(request):
    return Response({"message": "Hello for today! See you tomorrow!"})

@api_view(['GET'])
@schema(None)
def viewSchemaNone(request):
    return Response({"message": "Will not appear in schema!"})