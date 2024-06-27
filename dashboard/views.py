from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
# from django.core.exceptions import ObjectDoesNotExist

from datetime import date, timedelta
import numpy as np

from .models import Activity, Profile
from .forms import MetricsForm, ProfileForm

from pprint import pprint

# Create your views here.

def profile(request):
    """
    Display an individual :model:`dashboard.Profile`.

    **Context**

    ``profile``
        An instance of :model:`dashboard.Profile`.

    **Template:**

    :template:`dashboard/index.html`
    """

    if request.user.is_authenticated:

        user_profiles = Profile.objects.filter(user=request.user)
        print('USER PROFILES: ', user_profiles)

        # If user has profiles (existing user)
        if user_profiles.exists():
            user_last_profile =  user_profiles.latest('updated_on')
            username = user_last_profile.user
            print('USER: ', username)
            height = user_last_profile.height
            weight = user_last_profile.weight
            print(weight)
            weight_target = user_last_profile.weight_target
            birthdate = user_last_profile.birthdate   

            metrics_form = MetricsForm()
            profile_form = ProfileForm()

            # If the user updates the values
            if request.method == "POST":
                metrics_form = MetricsForm(data=request.POST)
                profile_form = ProfileForm(data=request.POST)

                # If user updates metrics form
                if metrics_form.is_valid() and username == request.user:
                    metrics = metrics_form.save(commit=False)
                    metrics.user_id = request.user.id
                    # get data from the form
                    user_last_profile.weight = metrics_form.cleaned_data.get('weight')
                    user_last_profile.weight_target = metrics_form.cleaned_data.get('weight_target')
                    weight, weight_target = user_last_profile.weight, user_last_profile.weight_target
                    # commit changes
                    user_last_profile.save() 
                    print('metrics form saved')

                    messages.add_message(
                        request, messages.SUCCESS,
                        'Your data has been updated!'
                        )
                
                if profile_form.is_valid() and username == request.user:
                    profile = profile_form.save(commit=False)
                    height = profile_form.cleaned_data.get('height')
                    birthdate = profile_form.cleaned_data.get('birthdate')

                    profile = Profile(height=height, weight=weight, 
                                birthdate=birthdate, weight_target=weight_target)

                    profile.save()
                    print('profile form saved')

                    messages.add_message(
                        request, messages.SUCCESS,
                        'Your data has been updated!'
                    )

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
                    'height': height,
                    'age': age,
                    'birthdate': birthdate,
                    'profile_form': profile_form,
                    'metrics_form': metrics_form,
                })


    else:
        return render(
            request,
            "dashboard/index.html",
        )


def create_profile(request):
    # New users with no profiles
    profile_form = ProfileForm()
    height = age = birthdate = None

    if request.method == "POST":
        profile_form = ProfileForm(data=request.POST)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user_id = request.user.id
            height = profile_form.cleaned_data.get('height')
            birthdate = profile_form.cleaned_data.get('birthdate')

            profile = Profile(height=height, weight=None, 
                        birthdate=birthdate, weight_target=None)

            profile.save()
            print('profile form saved')

            messages.add_message(
                request, messages.SUCCESS,
                'Your data has been created!'
            )

        age = (date.today() - birthdate) // timedelta(days=365.2425)

        bmi = bmi_target = bmi_rec = weight_rec \
            = classification = classification_target \
            = bmr = bmr_rec = bmr_target = None

    return render(
    request,
    "dashboard/profile.html",
    {
        'height': height,
        'age': age,
        'birthdate': birthdate,
        'profile_form': profile_form,
    })


# def profile_details(request):
    
#     # Filter by user
#     user_profiles = Profile.objects.filter(user=request.user)
#     # profile = Profile.objects.get(pk=1)
#     # profile = get_object_or_404(user_profiles, pk=1)

#     return render(
#         request,
#         "dashboard/profile.html",
#         )


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
        