from django.urls import path

from eq_app.views import EquipmentView

urlpatterns = [
    path('equipment/<int:id>/', EquipmentView.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    )),
    path('equipment/', EquipmentView.as_view(
        {'get': 'list', 'post': 'create'}
    )),
]