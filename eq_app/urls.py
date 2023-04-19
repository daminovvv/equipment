from django.urls import path
from rest_framework import routers
from eq_app.views import EquipmentViewSet, EquipmentTypeView

router = routers.SimpleRouter()
router.register(r'equipment', EquipmentViewSet)
urlpatterns = router.urls

urlpatterns += [
    path('equipment-type/', EquipmentTypeView.as_view({'get': 'list'})),
]
