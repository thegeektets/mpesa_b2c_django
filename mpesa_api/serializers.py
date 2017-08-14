from rest_framework import serializers

from mpesa_api.models import MpesaLog


class MpesaLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MpesaLog
        fields = '__all__'
