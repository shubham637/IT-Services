from django.urls import path

from . import views
from .views import CreateService, ServiceTemplate, ServiceListViewJson, ServiceUpdateView, ServiceDelete

urlpatterns = [
    path('test/', views.Test, name='test'),
    path('create/service/', CreateService.as_view(), name='create-service'),
    path('service/template/', ServiceTemplate.as_view(), name='service-template'),
    path('service/list/json/', ServiceListViewJson.as_view(), name='service-list-json'),
    path('service/update/<int:pk>', ServiceUpdateView.as_view(), name='service-update'),
    path('service/delete/<int:pk>', ServiceDelete.as_view(), name='service-delete'),
]