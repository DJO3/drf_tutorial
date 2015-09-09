from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetList, SnippetDetail, UserList, UserDetail, api_root, SnippetHighlight

urlpatterns = [
    url(r'^$', api_root),
    url(r'^snippets/$', SnippetList.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', SnippetHighlight.as_view(), name='snippet-highlight'),
    url(r'users/$', UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)

# Login and Logout views for browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
