from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UsersList, UsersDetail, EventsDetail, EventsList, GetUsers, GetEvents

#from .views import snippet_list
#from .views import snippet_detail
from api import views

urlpatterns = {
    url(r'^users/$', UsersList.as_view(), name="create"),
    url(r'^users/(?P<pk>[0-9]+)/$',UsersDetail.as_view(), name="details"),
    url(r'^events/$', EventsList.as_view()),
    url(r'^events/(?P<pk>[0-9]+)/$', EventsDetail.as_view()),
    url(r'^events/(?P<time>[past,present, future]+)/$', GetEvents.as_view()),
    url(r'^getusers/$', GetUsers.as_view()),
}

# urlpatterns = [
#     url(r'^users/$', snippet_list, name="create"),
#     url(r'^users/(?P<pk>[0-9]+)/$', snippet_detail, name="details"),
# ]


urlpatterns = format_suffix_patterns(urlpatterns)

