from django import forms
from .models import UserFile

class UserFileForm(forms.ModelForm):
    class Meta:
        model = UserFile
        fields = ['file']
        
    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            # Validators from model will run automatically
            # Additional custom validation can be added here
            return file