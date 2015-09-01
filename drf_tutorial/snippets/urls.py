from django.conf.urls import url
from snippets.views import snippet_list, snippet_detail

urlpatterns = [
    url(r'^snippets/$', snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail),
]
