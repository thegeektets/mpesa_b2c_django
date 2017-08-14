from user.models import User
from rest_framework import viewsets
from user.serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend,FilterSet
from rest_framework import generics, filters
import django_filters

#from django_searchbar.utils import SearchBar


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    class Filter(FilterSet):
        username = django_filters.CharFilter(name='username', lookup_expr='exact')
        username_like = django_filters.CharFilter(name='username', lookup_expr='icontains')

        class Meta:
            model = User
            fields = {
                'username': ['exact'],  # match w/ the lookup_expr?
                'username_like': ['icontains'],
            }

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    permission_class = (IsAuthenticated,)
    filter_class = Filter
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('username', 'email',)

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(UserViewSet, self).post(request, *args, **kwargs)
        else:
            content = {
                'status': 'request was not permitted'
            }
            return Response(content)
            # update , create , delete

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_staff:
            return super(UserViewSet, self).update(request, *args, **kwargs)
        else:
            content = {
                'status': 'request was not permitted'
            }
            return Response(content)

    def delete(self, request, pk, format=None):
        if request.user.is_superuser or request.user.is_staff:
            User = self.get_object(pk)
            User.delete()
            return Response(status=request.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'request is not permitted'
            }
            return Response(content)


