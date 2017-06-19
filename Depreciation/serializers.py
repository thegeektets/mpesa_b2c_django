from Depreciation.models import Assets , Depreciation
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']


class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = ['Name','Price','Assignee','SerialNumber','DepClass']

class DepreciationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depreciation
        fields = ['Class','Rate']