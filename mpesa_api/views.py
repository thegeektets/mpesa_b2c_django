import logging
import os
import json, requests

from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from rest_framework import permissions
from mpesa_api.models import MpesaLog
from mpesa_api.request import OAuth, B2C
from mpesa_api.serializers import MpesaLogSerializer
from rest_framework import status

class MpesaAPIViewSet(viewsets.ModelViewSet):
    queryset = MpesaLog.objects.all()
    serializer_class = MpesaLogSerializer
    permission_classes = (AllowAny, )


    def list(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_staff:
            b2c = B2C()
            r = b2c.fire(254702990800,100,'testdata','survey payout')
            return Response(r)
        else:
            raise PermissionDenied

    @list_route(methods=['post','get'])
    def call_back(self, request, **kwargs):

        if request.method == 'POST':
            result = json.dumps(request.data)
            result = result['Result']
            data = {
                'transactionid': result['TransactionID'],
                'resulttype': result['TransactionID'],
                'resultcode': result['ResultCode'],
                'resultdesc': result['ResultDesc'],
                'originatorconversationid':result['OriginatorConversationID'],
                'conversationid': result['ConversationID'],
                'referencedata': json.dumps(result['ReferenceData']),
            }
            serializer = MpesaLogSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:

            serializer = MpesaLogSerializer(instance=self.queryset, many=True)

            return Response(serializer.data)