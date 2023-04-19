from django.shortcuts import render
from rest_framework import mixins, viewsets, status, generics
from rest_framework.response import Response

from eq_app.models import EquipmentType, Equipment
from eq_app.serializers import EquipmentSerializer, EquipmentTypeSerializer


class EquipmentViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    lookup_field = 'id'

    def get_queryset(self):
        params = {'deleted': False, 'limit': None, 'offset': None}
        if self.action == "list":
            params.update(self.request.query_params.dict())
        del params['limit']
        del params['offset']
        return Equipment.objects.filter(**params)

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class EquipmentTypeView(mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = EquipmentTypeSerializer

    def get_queryset(self):
        params = {'limit': None, 'offset': None}
        if self.action == "list":
            params.update(self.request.query_params.dict())
        del params['limit']
        del params['offset']
        return EquipmentType.objects.filter(**params)
