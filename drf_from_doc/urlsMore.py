from django.urls import path
from . import viewsMore

urlpatterns = [
    path('', viewsMore.ListUsers.as_view()),
    path('hello/', viewsMore.hello_world),
    path('hello/getpost/', viewsMore.hello_world_get_post),
    path('throttleView/', viewsMore.throttleView),
    path('throttleViewSettings/', viewsMore.throttleViewSettings),
    path('throttleExampleView/', viewsMore.ThrottleExampleView.as_view()),
    path('throttle_example_view/', viewsMore.throttle_example_view),
]
