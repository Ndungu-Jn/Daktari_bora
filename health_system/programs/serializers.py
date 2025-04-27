from rest_framework import serializers
from .models import Program



class ProgramSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    
    class Meta:
        model = Program
        fields = ['id', 'name', 'description', 'category', 'duration', 'active', 'created_by', 'created_at']
