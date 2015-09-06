from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer


# Lists all Snippets
class SnippetList(ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


# Lists one Snippet based on primary key
class SnippetDetail(RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


# Lists all Users, read only
class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# List one User based on primary key, read only
class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer