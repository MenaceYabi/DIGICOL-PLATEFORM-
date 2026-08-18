from django.urls import path
from .import views

urlpatterns = [
    path('' , views.MembreDASH , name="dashboardmembre")
]