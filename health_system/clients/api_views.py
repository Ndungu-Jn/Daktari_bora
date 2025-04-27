from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Client, ClientProgram
from .serializers import ClientSerializer, ClientProgramSerializer

class ClientListCreate(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset = Client.objects.all()
        query = self.request.query_params.get('q', None)
        if query:
            queryset = queryset.filter(
                models.Q(first_name__icontains=query) | 
                models.Q(last_name__icontains=query)
            )
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ClientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClientProgramListCreate(generics.ListCreateAPIView):
    serializer_class = ClientProgramSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        client_id = self.kwargs['client_id']
        return ClientProgram.objects.filter(client_id=client_id)
    
    def perform_create(self, serializer):
        client_id = self.kwargs['client_id']
        client = get_object_or_404(Client, pk=client_id)
        serializer.save(client=client)

class ClientProgramRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientProgramSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        client_id = self.kwargs['client_id']
        return ClientProgram.objects.filter(client_id=client_id)