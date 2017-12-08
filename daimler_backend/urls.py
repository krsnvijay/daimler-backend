from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from push_notifications.api.rest_framework import GCMDeviceAuthorizedViewSet
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from accounts.views import UserViewSet, GroupViewSet, CurrentUserViewSet, LogEntryViewSet, StarredPartsViewSet
from critical_list.views import PartViewSet, PartStatusChangeViewSet, CriticalListViewSet, PartNotificationViewSet, \
    CriticalPartsViewSet
from critical_list.views import upload_file
from sos.views import SosViewSet, CommentViewSet, SosStatusChangeViewSet, SosSubscribeViewSet

import FrontEnd

schema_view = get_schema_view(title='Daimler API')
router = routers.DefaultRouter()
router.register(r'parts', PartViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'sos', SosViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'logs', LogEntryViewSet)
router.register(r'device/gcm', GCMDeviceAuthorizedViewSet)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^upload_file/$', upload_file, name='upload_file'),
    url(r'^api/', include(router.urls)),
    url(r'^api/schema/$', schema_view),
    url(r'^api/docs/', include_docs_urls(title='Daimler API Documentation', public=False)),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/current_user/$', CurrentUserViewSet.as_view(), name='current_user'),
    url(r'^api/critical_list/$', CriticalListViewSet.as_view(), name='critical_list'),
    url(r'^api/critical_list/critical_parts/$', CriticalPartsViewSet.as_view(), name='critical_list'),
    url(r'^api/critical_list/part_notification/$', PartNotificationViewSet.as_view(), name='part_notification'),
    url(r'^api/current_user/starred_parts/$', StarredPartsViewSet.as_view(), name='starred_parts'),
    url(r'^api/parts/(?P<pk>[^/.]+)/change_status/$', PartStatusChangeViewSet.as_view()),
    url(r'^api/sos/(?P<pk>[^/.]+)/change_status/$', SosStatusChangeViewSet.as_view()),
    url(r'^api/sos/(?P<pk>[^/.]+)/subscribe/$', SosSubscribeViewSet.as_view()),

    ###### FRONT-END URLs ######

    url(r'^', include('FrontEnd.urls')),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)