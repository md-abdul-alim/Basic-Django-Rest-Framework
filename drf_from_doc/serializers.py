from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet


class QuickUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class SnippetSerializer(serializers.ModelSerializer):
    # https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id', 'owner', 'title', 'code',
                  'linenos', 'language', 'style']


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']

# https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/


class HyperSnippetSerializer(serializers.HyperlinkedModelSerializer):
    # https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']


class HyperUserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
