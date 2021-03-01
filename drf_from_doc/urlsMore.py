from django.urls import include, path
from . import viewsMore

urlpatterns = [
    path('', viewsMore.ListUsers.as_view()),
    path('hello/', viewsMore.hello_world),
    path('hello/getpost/', viewsMore.hello_world_get_post),
]
