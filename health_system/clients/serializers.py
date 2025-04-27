from rest_framework import serializers
from .models import Client, ClientProgram
from programs.serializers import ProgramSerializer
from programs.models import Program

class ClientProgramSerializer(serializers.ModelSerializer):
    program_details = ProgramSerializer(source='program', read_only=True)
    program = serializers.PrimaryKeyRelatedField(queryset=Program.objects.all())

    
    class Meta:
        model = ClientProgram
        fields = ['id', 'program', 'program_details', 'enrollment_date', 'status']
        read_only_fields = ['enrollment_date']

class ClientSerializer(serializers.ModelSerializer):
    programs = ClientProgramSerializer(many=True, read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')
    
    class Meta:
        model = Client
        fields = [
            'id', 'first_name', 'last_name', 'date_of_birth', 'gender',
            'contact_number', 'street_address', 'city', 'state', 'zip_code',
            'created_by', 'created_at', 'updated_at', 'programs'
        ]