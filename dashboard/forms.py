from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button, Field, MultiField, Div
from django.shortcuts import reverse
from .models import Profile, Activity, Nutrition

class MetricsForm(forms.ModelForm):

    # helper form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submitMetrics', 'Submit', css_class='btn-success'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-secondary',
            onclick="window.location.href = '{}';".format(reverse('home'))))

    class Meta:
        model = Profile
        fields = ('weight','weight_target')
        labels = {
            'weight': 'Weight (Kg)',
            'weight_target': 'Target Weight (Kg)',
        }


class ProfileForm(forms.ModelForm):
    """
    Form based on the profile custom model
    """
    birthdate = forms.DateField(input_formats=['%d-%m-%Y'])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submitProfile', 'Submit', css_class='btn-success'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-secondary',
            onclick="window.location.href = '{}';".format(reverse('profile'))))

    class Meta:
        model = Profile
        fields = ('height', 'profile_image')
        labels = {
            'height': 'Height (cm)',
        }


class ActivityForm(forms.ModelForm):
    """
    Form based on the activity custom model
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.layout = Layout(
            Field('activity_type', oninput="fetchCaloriesBurnt()",),
            Div(css_class="mb-3", css_id="activity_list"),
            ('duration'), ('distance')
            )

        self.helper.add_input(Submit('submitActivity', 'Submit', css_class='btn-success submit'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-secondary',
            onclick="window.location.href = '{}';".format(reverse('home'))))

    class Meta:
        model = Activity
        fields = ('activity_type', 'distance', 'duration')
        labels = {
            'activity_type': 'Activity',
            'duration': 'Duration (min)',
            'distance': 'Distance (km)',
        }


class NutritionForm(forms.ModelForm):
    """
    Form based on the activity custom model
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.add_input(Submit('submitNutrition', 'Submit', css_class='btn-success submit'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-secondary',
            onclick="window.location.href = '{}';".format(reverse('home'))))

    class Meta:
        model = Nutrition
        fields = ('food_item', 'portion')
        labels = {
            'food_item': 'Food',
            'portion': 'Serving (g)',
        }


class FullForm(forms.Form):
    """
    Form that contains fields from several models
    for the user to fill out after signing up
    """
    height = forms.FloatField(
        label = "Height (cm)",
        required = True,
        )

    weight = forms.FloatField(
        label = "Weight (kg)",
        required = True,
        )

    weight_target = forms.FloatField(
        label = "Target Weight (kg)",
        required = True,
        )
        
    birthdate = forms.DateField(
        input_formats=['%d-%m-%Y'],
        required = True,
        )
    
    activity_type = forms.CharField(
        max_length = 200,
        required = True,
        )
    
    duration = forms.FloatField(
        label = "Duration (min)",
        required = True,
        )

    distance = forms.FloatField(
        label = "Distance (km)",
        required = False,
        )
    
    food_item = forms.CharField(
        label = "Food",
        required = True,
        )

    portion = forms.IntegerField(
        label = "Serving (g)",
        required = True,
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['height'].widget.attrs['min'], \
            self.fields['height'].widget.attrs['max'] = 1, 999
        self.fields['weight'].widget.attrs['min'], \
            self.fields['weight'].widget.attrs['max'] = 1, 999
        self.fields['weight_target'].widget.attrs['min'], \
            self.fields['weight_target'].widget.attrs['max'] = 1, 999
        self.fields['duration'].widget.attrs['min'], \
            self.fields['duration'].widget.attrs['max'] = 1, 999
        self.fields['distance'].widget.attrs['min'], \
            self.fields['distance'].widget.attrs['max'] = 1, 999
        self.fields['food_item'].widget.attrs['patern'] = '^[a-zA-Z]+$'
        self.fields['portion'].widget.attrs['min'], \
            self.fields['portion'].widget.attrs['max'] = 1, 2999

        # Layout
        self.helper.layout = Layout(
            ('height'), ('weight'), ('weight_target'), ('birthdate'),
            Field('activity_type', oninput="fetchCaloriesBurnt()",),
            Div(css_class="mb-3", css_id="activity_list"),
            ('duration'), ('distance'), (food_item), (portion),
            )
        
        # Buttons
        self.helper.add_input(Submit('submitFull', 'Submit', css_class='btn-success'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-secondary',
            onclick="window.location.href = '{}';".format(reverse('home'))))