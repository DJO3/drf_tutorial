from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


# Lists all Snippets
class SnippetList(ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


# Lists one Snippet based on primary key
class SnippetDetail(RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer



