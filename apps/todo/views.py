from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import generics

from apps.todo.models import ToDo 
from apps.todo.serializers import ToDoSerializer
from apps.todo.permissions import ToDoPermission

# Create your views here.
class ToDoAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (IsAuthenticated, )

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['user', 'title', 'description', 'is_completed']
    search_fields = ['user__username', 'title', 'description']
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (ToDoPermission(), )
        return (AllowAny(), )
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class ToDoAllDelete(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    
    def delete(self, request, *args, **kwargs):
        todo = ToDo.objects.filter(user=request.user)
        todo.delete()
        return Response({'delete' : 'Все такски удалены !!!!'})