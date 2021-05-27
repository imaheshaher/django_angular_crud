from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from .serializers import EmployeeSerializer
from .models import Employee
class EmployeeView(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = []
