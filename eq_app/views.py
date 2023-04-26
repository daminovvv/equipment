from rest_framework import mixins
from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from eq_app.models import Equipment
from eq_app.models import EquipmentType
from eq_app.serializers import EquipmentSerializer
from eq_app.serializers import EquipmentTypeSerializer
from eq_app.services import process_query_params


class EquipmentViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Allows to work with equipment"""

    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    lookup_field = "id"
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Filters and returns queryset for serializer"""
        params = process_query_params(self, soft_delete=True)
        return Equipment.objects.filter(**params)

    def create(self, request, *args, **kwargs):
        """Creates records in the database"""
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class EquipmentTypeView(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Allows to work with equipment type"""

    serializer_class = EquipmentTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Filters and returns queryset for serializer"""
        params = process_query_params(self)
        return EquipmentType.objects.filter(**params)
