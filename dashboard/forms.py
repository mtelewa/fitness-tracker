from .models import Profile
from django import forms

class MetricsForm(forms.ModelForm):
    birthdate = forms.DateField(input_formats=['%d-%m-%Y'], initial='dd-mm-yyyy')

    class Meta:
        model = Profile
        fields = ('height','weight','profile_image','birthdate')