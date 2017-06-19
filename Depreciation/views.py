from Depreciation.models import Assets,Depreciation
from django.contrib.auth.models import User
from rest_framework import viewsets
from Depreciation.serializers import UserSerializer, DepreciationSerializer , AssetsSerializer

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

class DepreciationViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows Depreciation to be viewed or edited.
    """
    queryset = Depreciation.objects.all()
    serializer_class = DepreciationSerializer




