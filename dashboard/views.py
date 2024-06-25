from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from datetime import date, timedelta
import numpy as np

from .models import Activity, Profile
from .forms import MetricsForm, ProfileForm


# Create your views here.

# def index(request):
#     return HttpResponse('Hi. I am working!')

def dashboard(request):
    """
    Display an individual :model:`dashboard.Profile`.

    **Context**

    ``profile``
        An instance of :model:`dashboard.Profile`.

    **Template:**

    :template:`dashboard/index.html`
    """

    if request.user.is_authenticated:

        # Update foreign key
        profile = Profile.objects.get(pk=1)
        Profile.objects.all().update(user=profile)

        # Filter by user
        user = Profile.objects.filter(user=request.user)
        
        # If user has previous entries i.e. existing user
        # use their last entry else set to None
        try:
            queryset =  user.latest('updated_on')
            height = queryset.height
            weight = queryset.weight
            weight_target = queryset.weight_target
            birthdate = queryset.birthdate
        except ObjectDoesNotExist:
            height = weight =  weight_target = birthdate = None

        metrics_form = MetricsForm()

        # If the user updates the values
        if request.method == "POST":
            metrics_form = MetricsForm(data=request.POST)

            if metrics_form.is_valid() and queryset.user == request.user:
                # profile = metrics_form.save(commit=False)
                weight = metrics_form.cleaned_data.get('weight')
                weight_target = metrics_form.cleaned_data.get('weight_target')

                profile = Profile(height=height, weight=weight, 
                            birthdate=birthdate, weight_target=weight_target)

                profile.save()

                messages.add_message(
                    request, messages.SUCCESS,
                    'Your values have been updated!'
                    )

        if weight is not None:
            # Body Mass Index (BMI)
            bmi = np.round(weight / (height/100)**2, 2) # kg/m2
            bmi_target = np.round(weight_target/ (height/100)**2, 2) # kg/m2
            bmi_rec = 24

            weight_rec =  np.round(bmi_rec * (height/100)**2)

            # Classification
            classification = get_classification(bmi)
            classification_target = get_classification(bmi_target)

            # Age
            age = (date.today() - birthdate) // timedelta(days=365.2425)

            # Basal Metabolic Rate (BMR)
            # Revised Harris-Benedict Equation (for Men - just for illustration)
            bmr = np.round(13.397 * weight + 4.799 * height - 5.677 * age + 88.362)
            bmr_rec = np.round(13.397 * weight_rec + 4.799 * height - 5.677 * age + 88.362)
            bmr_target = np.round(13.397 * weight_target + 4.799 * height - 5.677 * age + 88.362)

        else:
            bmi = bmi_target = bmi_rec = weight_rec \
                = classification = classification_target \
                = age = bmr = bmr_rec = bmr_target = None

        return render(
            request,
            "dashboard/index.html",
            {
                'bmi': bmi,
                'bmi_rec': bmi_rec,
                'bmi_target': bmi_target,
                'bmr': bmr,
                'bmr_rec': bmr_rec,
                'bmr_target': bmr_target,
                'weight': weight,
                'weight_rec': weight_rec,
                'weight_target': weight_target,
                'classification': classification,
                'classification_target': classification_target,
                'metrics_form': metrics_form,
            })
    
    else:
        return render(
            request,
            "dashboard/index.html",
        )



def profile(request):
    """
    Display an individual :model:`dashboard.Profile`.

    **Context**

    ``profile``
        An instance of :model:`dashboard.Profile`.

    **Template:**

    :template:`dashboard/profile.html`
    """

    # Update foreign key
    profile = Profile.objects.get(pk=1)
    Profile.objects.all().update(user=profile)

    # Filter by user
    user = Profile.objects.filter(user=request.user)
    
    # If user has previous entries i.e. existing user
    # use their last entry else set to None
    try:
        queryset =  user.latest('updated_on')
        height = queryset.height
        weight = queryset.weight
        weight_target = queryset.weight_target
        birthdate = queryset.birthdate
    except ObjectDoesNotExist:
        height = weight =  weight_target = birthdate = None

    profile_form = ProfileForm()

    # If the user updates the values
    if request.method == "POST":
        profile_form = ProfileForm(data=request.POST)

        if profile_form.is_valid() and queryset.user == request.user:
            height = profile_form.cleaned_data.get('height')
            birthdate = profile_form.cleaned_data.get('birthdate')

            profile = Profile(height=height, weight=weight, 
                        birthdate=birthdate, weight_target=weight_target)

            profile.save()

            messages.add_message(
                request, messages.SUCCESS,
                'Your data has been updated!'
                )
    
    if height is not None:
        # Age
        age = (date.today() - birthdate) // timedelta(days=365.2425)
    else:
        height = age = birthdate = None

    return render(
        request,
        "dashboard/profile.html",
        {
            'height': height,
            'age': age,
            'birthdate': birthdate,
            'profile_form': profile_form,
        })


def calendar(request):
    """
    Display an individual :model:`dashboard.Profile`.

    **Context**

    ``profile``
        An instance of :model:`dashboard.Profile`.

    **Template:**

    :template:`dashboard/profile_details.html`
    """


    return render(
        request,
        "dashboard/calendar.html",
        {
            'API_KEY': settings.API_KEY,
            'CLIENT_ID': settings.CLIENT_ID,
        })


def get_classification(bmi):

    if bmi < 16:
        classification = 'Severe Thinness'
    elif bmi >= 16 and bmi < 17:
        classification = 'Moderate Thinness'
    elif bmi >= 17 and bmi < 18.5:
        classification = 'Mild Thinness'
    elif bmi >= 18.5 and bmi < 25:
        classification = 'Normal'
    elif bmi >= 25 and bmi < 30:
        classification = 'Overweight'
    elif bmi >= 30 and bmi < 35:
        classification = 'Obese Class I'
    elif bmi >=35 and bmi < 40:
        classification = 'Obese Class II'
    else:
        classification = 'Obese Class III'
    
    return classification
        