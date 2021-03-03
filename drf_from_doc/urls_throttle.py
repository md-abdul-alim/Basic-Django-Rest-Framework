from django.urls import path
from . import views_throttle

urlpatterns = [
    path('', views_throttle.ListUsers.as_view()),
    path('hello/', views_throttle.hello_world),
    path('hello/getpost/', views_throttle.hello_world_get_post),

    path('throttleView/', views_throttle.throttleView),
    path('throttleViewSettings/', views_throttle.throttleViewSettings),
    path('throttleExampleView/', views_throttle.ThrottleExampleView.as_view()),
    path('throttle_example_view/', views_throttle.throttle_example_view),

    path('viewSchema/', views_throttle.viewSchema),
    path('viewSchemaNone/', views_throttle.viewSchemaNone),
]
