from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings

from datetime import date, timedelta
import numpy as np
from pprint import pprint
import requests

from .models import Activity, Profile
from .forms import MetricsForm, ProfileForm, FullForm, ActivityForm

# Create your views here.

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
        user_profiles = Profile.objects.filter(user=request.user)
        # print('USER PROFILES: ', user_profiles)

        user_activities = Activity.objects.filter(user=request.user)
        # print('USER Activities: ', user_activities)

        # If user has profiles (existing user)
        if user_profiles.exists():
            # Profile card
            user_last_profile =  user_profiles.latest('updated_on')
            username = user_last_profile.user
            weight = user_last_profile.weight
            height = user_last_profile.height
            birthdate = user_last_profile.birthdate
            weight_target = user_last_profile.weight_target
            profile_image = user_last_profile.profile_image

            # Activity card
            user_last_activity = user_activities.latest('activity_on')
            activity_type = user_last_activity.activity_type
            distance = user_last_activity.distance
            duration = user_last_activity.duration

            metrics_form = MetricsForm()

            # If the user updates the values
            if request.method == "POST" and 'submitMetrics' in request.POST:
                metrics_form = MetricsForm(data=request.POST)

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
                    
                    return redirect('home')

            metrics_form = MetricsForm()

            # If the user updates the values
            if request.method == "POST" and 'submitMetrics' in request.POST:
                metrics_form = MetricsForm(data=request.POST)

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
                    
                    return redirect('home')

            # Calories Burnt API
            api_url = f'https://api.api-ninjas.com/v1/caloriesburned?activity={activity_type}'
            response = requests.get(api_url, headers={'X-Api-Key': settings.CAL_BURN_API_KEY})
            if response.status_code == requests.codes.ok:
                activity_list = response.json()
                activities = [d['name'] for d in activity_list if 'name' in d]
            else:
                print("Error:", response.status_code, response.text)

            activity_form = ActivityForm()

            # If the user updates the values
            if request.method == "POST" and 'submitActivity' in request.POST:
                print('POST is executed')
                activity_form = ActivityForm(data=request.POST)

                # If user updates activity form
                if activity_form.is_valid() and username == request.user:
                    activity = activity_form.save(commit=False)
                    activity.user_id = request.user.id

                    # get data from the form
                    user_last_activity.activity_type = activity_form.cleaned_data.get('activity_type')
                    user_last_activity.duration = activity_form.cleaned_data.get('duration')
                    user_last_activity.distance = activity_form.cleaned_data.get('distance')
                    activity_type, duration, distance = user_last_activity.activity_type, \
                                                   user_last_activity.activity_duration, \
                                                   user_last_activity.activity_distance,

                    # commit changes
                    user_last_activity.save() 
                    print('activity form saved')

                    messages.add_message(
                        request, messages.SUCCESS,
                        'Your data has been updated!'
                        )
                    
                    return redirect('home')            


            
            weight_rec = get_metrics(height,weight,birthdate)['weight_rec']

            bmi, bmi_target, bmi_rec =  \
                        get_metrics(height,weight,birthdate)['bmi'], \
                        get_metrics(height,weight_target,birthdate)['bmi'], 24
            
            bmr, bmr_target, bmr_rec =  \
                        get_metrics(height,weight,birthdate)['bmr'], \
                        get_metrics(height,weight_target,birthdate)['bmr'], \
                        get_metrics(height,weight_rec,birthdate)['bmr']

            classification, classification_target = \
                        get_metrics(height,weight,birthdate)['classification'], \
                        get_metrics(height,weight_target,birthdate)['classification']


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
                    'profile_image': profile_image,
                    'metrics_form': metrics_form,
                    'activity': activity_type,
                    'duration': duration,
                    'distance': distance,
                    'activity_form': activity_form,
                })

        else:
            dict = profile_create(request)
            return render(
                request,
                "dashboard/profile_create.html",
                dict)

    else:
        return render(
            request,
            "dashboard/index.html",
        )


def profile_create(request):
    
    full_form = FullForm()
    height = age = weight = weight_target = None

    if request.method == "POST":
        full_form = FullForm(data=request.POST)

        if full_form.is_valid():
            profile = full_form.save(commit=False)
            height = full_form.cleaned_data.get('height')
            birthdate = full_form.cleaned_data.get('birthdate')
            weight = full_form.cleaned_data.get('weight')
            weight_target = full_form.cleaned_data.get('weight_target')
                
            Profile.objects.create(user=request.user, height=height, weight=weight, 
                                birthdate=birthdate, weight_target=weight_target)

            age = (date.today() - birthdate) // timedelta(days=365.2425)
            print('full form saved')

            messages.add_message(
                request, messages.SUCCESS,
                'Your data has been created!'
            )

    dict = {
            'height': height,
            'weight': weight,
            'age': age,
            'full_form': full_form,
            }

    return dict


def profile_update(request):

    if request.user.is_authenticated:
        user_profiles = Profile.objects.filter(user=request.user)

        # If user has profiles (existing user)
        if user_profiles.exists():
            user_last_profile =  user_profiles.latest('updated_on')
            username = user_last_profile.user
            height = user_last_profile.height
            birthdate = user_last_profile.birthdate
            age = (date.today() - birthdate) // timedelta(days=365.2425)
            weight = user_last_profile.weight
            profile_image = user_last_profile.profile_image

            profile_form = ProfileForm()

            # If the user updates the values
            if request.method == "POST":
                profile_form = ProfileForm(data=request.POST, files=request.FILES, instance=user_last_profile)

                if profile_form.is_valid() and username == request.user:
                    profile = profile_form.save(commit=False)

                    profile.user_id = request.user.id
                    # get data from the form
                    user_last_profile.height = profile_form.cleaned_data.get('height')
                    height = user_last_profile.height

                    user_last_profile.birthdate = profile_form.cleaned_data.get('birthdate')
                    age = (date.today() - user_last_profile.birthdate) // timedelta(days=365.2425)

                    user_last_profile.profile_image = profile_form.cleaned_data.get('profile_image')
                    profile_image = user_last_profile.profile_image

                    # commit changes
                    user_last_profile.save() 
                    print('profile form saved')

                    messages.add_message(
                        request, messages.SUCCESS,
                        'Your data has been updated!'
                        )

                    return redirect('profile')
        
            return render(
                request,
                "dashboard/profile.html",
                {
                    'height': height,
                    'weight': weight,
                    'age': age,
                    'profile_image': profile_image,
                    'profile_form': profile_form,
                })
        
        else:
            dict = profile_create(request)
            return render(
                request,
                "dashboard/profile_create.html",
                dict)
    
    else:
        return render(
            request,
            "dashboard/index.html",
        )


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
            'GOOGLE_API_KEY': settings.GOOGLE_API_KEY,
            'CLIENT_ID': settings.CLIENT_ID,
        })


def get_metrics(height, weight, birthdate):

    # Body Mass Index (BMI)
    bmi = np.round(weight / (height/100)**2, 2) # kg/m2

    # recommended weight
    weight_rec =  np.round(24 * (height/100)**2)

    # Age
    age = (date.today() - birthdate) // timedelta(days=365.2425)

    # Basal Metabolic Rate (BMR)
    # Revised Harris-Benedict Equation (for Men - just for illustration)
    bmr = np.round(13.397 * weight + 4.799 * height - 5.677 * age + 88.362)

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
    
    return {
            'bmi': bmi,
            'bmr': bmr,
            'weight_rec': weight_rec,
            'classification': classification
            }
        