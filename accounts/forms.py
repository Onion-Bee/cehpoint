from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Company

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['user', 'is_profile_completed', 'created_at', 'updated_at']
        widgets = {
            'company_description': forms.Textarea(attrs={'rows': 4}),
            'year_established': forms.NumberInput(attrs={'min': 1900, 'max': 2025}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            if field in ['social_media_linkedin', 'social_media_twitter']:
                self.fields[field].required = False 