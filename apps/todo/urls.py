from rest_framework.routers import DefaultRouter
from django.urls import path
from apps.todo.views import ToDoAPIViewSet, ToDoAllDelete

router = DefaultRouter()
router.register('todo', ToDoAPIViewSet, 'api_todo')

urlpatterns = [
    path('all_delete', ToDoAllDelete.as_view(), name="all_delete")
]
urlpatterns += router.urls 

