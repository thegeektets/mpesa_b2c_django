from Depreciation.models import Assets,Depreciation
from django.contrib.auth.models import User
from rest_framework import viewsets
from Depreciation.serializers import UserSerializer, DepreciationSerializer , AssetsSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_class = (IsAuthenticated)

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


class AssetsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Assets to be viewed or edited.
    """
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(AssetsViewSet, self).post(request, *args, **kwargs)
        else:
            content = {
                'status': 'request was not permitted'
            }
            return Response(content)
    #update , create , delete

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_staff:
            return super(AssetsViewSet, self).update(request, *args, **kwargs)
        else:
            content = {
                'status': 'request was not permitted'
            }
            return Response(content)

    def delete(self, request, pk, format=None):
        if request.user.is_superuser or request.user.is_staff:
            Assets = self.get_object(pk)
            Assets.delete()
            return Response(status=request.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'request is not permitted'
            }
            return Response(content)


class DepreciationViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows Depreciation to be viewed or edited.
    """
    queryset = Depreciation.objects.all()
    serializer_class = DepreciationSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(DepreciationViewSet, self).post(request, *args, **kwargs)
        else:
            content = {
                'status': 'request was not permitted'
            }
            return Response(content)

    # update , create , delete

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_staff:
            return super(DepreciationViewSet, self).update(request, *args, **kwargs)
        else:
            content = {
                'status': 'request was not permitted'
            }
            return Response(content)

    def delete(self, request, pk, format=None):
        if request.user.is_superuser or request.user.is_staff:
            Depreciation = self.get_object(pk)
            Depreciation.delete()
            return Response(status=request.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'request is not permitted'
            }
            return Response(content)


