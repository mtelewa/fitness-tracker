from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from django.shortcuts import reverse
from .models import Profile

class MetricsForm(forms.ModelForm):

    weight_target = forms.FloatField(
        label = "Target Weight",
        required = True,
        )

    class Meta:
        model = Profile
        fields = ('weight',)

    # helper form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_class = 'forms'
        
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-secondary',
            onclick="window.location.href = '{}';".format(reverse('home'))))


class ProfileForm(forms.ModelForm):
    birthdate = forms.DateField(input_formats=['%d-%m-%Y'])

    class Meta:
        model = Profile
        fields = ('height', 'profile_image', )

    # helper form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-secondary',
            onclick="window.location.href = '{}';".format(reverse('profile'))))