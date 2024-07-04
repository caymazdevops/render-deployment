from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Sport
from .serializers import SportSerializer

class SportListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

