from django import forms
from .models import Client, ClientProgram
from programs.models import Program

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'first_name', 'last_name', 'date_of_birth', 'gender',
            'contact_number', 'street_address', 'city', 'state', 'zip_code'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class ClientProgramForm(forms.ModelForm):
    program = forms.ModelChoiceField(
        queryset=Program.objects.none(),  # Start with empty queryset
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = ClientProgram
        fields = ['program', 'status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'})
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user from kwargs
        super(ClientProgramForm, self).__init__(*args, **kwargs)
        
        # Filter programs by the current user
        if user:
            self.fields['program'].queryset = Program.objects.filter(created_by=user)