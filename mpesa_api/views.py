import logging
import os
from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated

from mpesa_api.models import MpesaLog
from mpesa_api.request import OAuth, B2C
from mpesa_api.serializers import MpesaLogSerializer
from rest_framework import status

class IsCreationOrIsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated():
            if view.action == 'create':
                return True
            else:
                return False
        else:
            return True

class MpesaAPIViewSet(viewsets.ModelViewSet):
    queryset = MpesaLog.objects.all()
    serializer_class = MpesaLogSerializer
    permission_classes = (IsCreationOrIsAuthenticated, )


    def list(self, request, *args, **kwargs):
        b2c = B2C()
        r = b2c.fire(254702990800,100,'testdata','survey payout')
        return Response(r)

    @list_route(methods=['post','get'])
    def call_back(self, request, **kwargs):
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, 'api_log.txt')
        logging.basicConfig(filename=file_path, level=logging.DEBUG)
        logging.debug('log')
        logging.info(request.data)

        if request.method == 'POST':
            data = {
                'request': request.data['request'],
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