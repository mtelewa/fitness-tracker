from .models import Profile
from django import forms

class MetricsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('height','weight','profile_image','birthdate')