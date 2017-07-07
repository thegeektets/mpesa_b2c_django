from Depreciation.models import Assets , Depreciation
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email', 'first_name', 'last_name']


class DepreciationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depreciation
        fields = ['id','Class','Rate']

class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = ['id','title','price','doa','assignee','assignee_id','serialnumber','depreciation_id' , 'depreciation']

    depreciation = DepreciationSerializer(read_only=True)
    depreciation_id = serializers.UUIDField(read_only=False)
    assignee = UserSerializer(read_only=True)
    assignee_id = serializers.UUIDField(read_only=False)


