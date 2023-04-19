from django.urls import path
from rest_framework import routers
from eq_app.views import EquipmentView

router = routers.SimpleRouter()
router.register(r'equipment', EquipmentView)
urlpatterns = router.urls
