from django import forms
from .models import Program

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['name', 'description', 'category', 'duration', 'active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
