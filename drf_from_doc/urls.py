from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework import renderers

# https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/
# Binding ViewSets to URLs explicitly
snippet_list_viewSet = views.SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail_viewSet = views.SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight_viewSet = views.SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list_viewSet = views.UserViewSet.as_view({
    'get': 'list'
})
user_detail_viewSet = views.UserViewSet.as_view({
    'get': 'retrieve'
})

router = routers.DefaultRouter()
router.register('users', views.QuickUserViewSet)
router.register('groups', views.QuickGroupViewSet)
router.register('usersViewSet', views.SnippetViewSet)
router.register('snippetsViewSet', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>', views.snippet_detail),

    path('class/snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('class/snippets/<int:pk>',
         views.SnippetDetail.as_view(), name='snippet-detail'),

    path('mixins/class/snippets/', views.SnippetList.as_view()),
    path('mixins/class/snippets/<int:pk>', views.SnippetDetail.as_view()),

    path('generic/class/snippets/', views.SnippetList.as_view()),
    path('generic/class/snippets/<int:pk>', views.SnippetDetail.as_view()),

    path('user/', views.UserList.as_view(), name='user-list'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

    path('api_root/', views.api_root),

    path('snippets/<int:pk>/highlight/',
         views.SnippetHighlight.as_view(), name='snippet-highlight'),

    path('hyper/class/snippets/', views.HyperSnippetList.as_view(),
         name='hyper-snippet-list'),
    path('hyper/class/snippets/<int:pk>',
         views.HyperSnippetDetail.as_view(), name='hyper-snippet-detail'),

    path('hyper/user/', views.HyperUserList.as_view(), name='hyper-user-list'),
    path('hyper/user/<int:pk>/', views.HyperUserDetail.as_view(),
         name='hyper-user-detail'),
]
