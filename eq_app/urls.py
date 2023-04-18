from django.urls import path

from eq_app.views import EquipmentView

urlpatterns = [
    path('equipment/', EquipmentView.as_view(
        {'get': 'list', 'post': 'create'}
    )),
]