from Depreciation.models import Assets,Depreciation
from django.contrib.auth.models import User
from rest_framework import viewsets
from Depreciation.serializers import UserSerializer, DepreciationSerializer , AssetsSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser ,IsAuthenticated
from rest_framework.response import Response




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class AssetsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Assets to be viewed or edited.
    """
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer
    permission_classes = (IsAuthenticated,)


    #update , create , delete
    def update(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_staff:
            return super(AssetsViewSet, self).update(request, *args, **kwargs)
        else:
            content = {
                'status': 'request was permitted'
            }
            return Response(content)

class DepreciationViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows Depreciation to be viewed or edited.
    """
    queryset = Depreciation.objects.all()
    serializer_class = DepreciationSerializer




