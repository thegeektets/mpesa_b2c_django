from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from Depreciation.views import UserViewSet, AssetsViewSet, DepreciationViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet, base_name='users')
router.register(r'assets', AssetsViewSet, base_name='assets')
router.register(r'depreciation',DepreciationViewSet, base_name='depreciation')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
]