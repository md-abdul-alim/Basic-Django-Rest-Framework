from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>', views.snippet_detail),

    path('class/snippets/', views.SnippetList.as_view()),
    path('class/snippets/<int:pk>', views.SnippetDetail.as_view()),

    path('mixins/class/snippets/', views.SnippetList.as_view()),
    path('mixins/class/snippets/<int:pk>', views.SnippetDetail.as_view()),

    path('generic/class/snippets/', views.SnippetList.as_view()),
    path('generic/class/snippets/<int:pk>', views.SnippetDetail.as_view()),
]
