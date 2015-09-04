from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetList, snippet_detail

urlpatterns = [
    url(r'^snippets/$', SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
