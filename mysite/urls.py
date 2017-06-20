from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from Depreciation.views import UserViewSet , AssetsViewSet , DepreciationViewSet

from rest_framework.authtoken import views as rest_framework_views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'assets', AssetsViewSet)
router.register(r'depreciation', DepreciationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]