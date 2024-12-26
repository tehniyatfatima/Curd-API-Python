from django.shortcuts import render

# todo/views.py

from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
#from rest_framework.permissions import IsAuthenticated

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    #permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save()
