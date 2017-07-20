from Depreciation.models import Assets , Depreciation , User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class DepreciationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Depreciation
        fields = '__all__'


class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = ['id','title','price','doa','assignee','assignee_id','serialnumber','depreciation_id' , 'depreciation']

    depreciation = DepreciationSerializer(read_only=True)
    depreciation_id = serializers.UUIDField(read_only=False)
    assignee = UserSerializer(read_only=True)
    assignee_id = serializers.UUIDField(read_only=False)



