from django.contrib.auth.models import User
from rest_framework import viewsets
from Depreciation.models import Assets, Depreciation
from Depreciation.serializers import UserSerializer, AssetsSerializer, DepreciationSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DepreciationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Depreciation.objects.all()
    serializer_class = DepreciationSerializer


class AssetsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer


