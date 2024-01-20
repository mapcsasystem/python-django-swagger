from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task


@extend_schema_view(
    list=extend_schema(description='Muestra lista de task'),
    retrieve=extend_schema(description='Muestra una task'),
    create=extend_schema(description='Crea una task'),
    update=extend_schema(description='Actualiza una task'),
    destroy=extend_schema(description='Elimina una task'),
)
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = []
