from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('PRESIDENT', 'President'),
        ('MINISTER', 'Minister'),
        ('CHANCELLOR', 'Chancellor'),
        ('VOTER', 'Voter'),
    ]
    
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect,
        label="Register as",
        initial='VOTER',
    )
    
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Date of Birth",
        required=True,
    )
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'role', 'date_of_birth')
    
    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            user.userprofile.role = self.cleaned_data.get('role')
            user.userprofile.date_of_birth = self.cleaned_data.get('date_of_birth')
            user.userprofile.save()
        return user 