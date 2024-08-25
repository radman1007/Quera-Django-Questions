from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
    
    def clean_national_code(self):
        national_code = self.changed_data.get('national_code')
        if len(national_code) == 10:
            return national_code
        else:
            raise ValidationError('national code must be 10 character')
        
    def clean_fullname(self):
        fullname = self.cleaned_data.get('fullname')
        parts = fullname.split(' ')
        if len(parts) != 2:
            raise ValidationError('you must use space in fullname')
        first_name, last_name = parts
        if not (first_name.istitle() and last_name.istitle()):
            raise ValidationError("you must use big letter for first character")
        return fullname