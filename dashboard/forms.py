from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button, Field, MultiField, Div
from django.shortcuts import reverse
from .models import Profile, Activity


class MetricsForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('weight','weight_target')
        labels = {
            'weight': 'Weight (Kg)',
            'weight_target': 'Target Weight (Kg)',
        }

    # helper form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        
        self.helper.add_input(Submit('submitMetrics', 'Submit', css_class='btn-success'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-secondary',
            onclick="window.location.href = '{}';".format(reverse('home'))))


class ProfileForm(forms.ModelForm):
    birthdate = forms.DateField(input_formats=['%d-%m-%Y'])

    class Meta:
        model = Profile
        fields = ('height', 'profile_image')
        labels = {
            'height': 'Height (cm)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        
        self.helper.add_input(Submit('submitProfile', 'Submit', css_class='btn-success'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-secondary',
            onclick="window.location.href = '{}';".format(reverse('profile'))))


class FullForm(forms.ModelForm):
    birthdate = forms.DateField(input_formats=['%d-%m-%Y'])

    class Meta:
        model = Profile
        fields = ('height', 'weight', 'weight_target', 'birthdate', 'profile_image')
        labels = {
            'height': 'Height (cm)',
            'weight': 'Weight (Kg)',
            'weight_target': 'Target Weight (Kg)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        
        self.helper.add_input(Submit('submitFull', 'Submit', css_class='btn-success'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-secondary',
            onclick="window.location.href = '{}';".format(reverse('home'))))


class ActivityForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # activities = kwargs.pop('activities', [])
        super().__init__(*args, **kwargs)
        # self.fields['activity_type'].choices = [(count, activity) for count, activity in enumerate(activities)]
        self.helper = FormHelper(self)
        
        self.helper.add_input(Submit('submitActivity', 'Submit', css_class='btn-success submit'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-secondary',
            onclick="window.location.href = '{}';".format(reverse('home'))))
        
        self.helper.layout = Layout(
            Field('activity_type', oninput="fetchCaloriesBurnt()",),
            Div(css_class="mb-3", css_id="activity_list"),
            ('duration'), ('distance')
            )

    class Meta:
        model = Activity
        fields = ('activity_type', 'distance', 'duration')
        labels = {
            'activity_type': 'Activity',
            'duration': 'Duration (min)',
            'distance': 'Distance (km)',
        }

