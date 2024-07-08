# Django modules
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
# Other external modules
from datetime import date, timedelta
import matplotlib.pyplot as plt
import mplcyberpunk
from io import StringIO
import seaborn as sns
import numpy as np
import requests
import os
# Local imports
from .models import Activity, Profile, Nutrition
from .forms import MetricsForm, ProfileForm, FullForm, ActivityForm, NutritionForm


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
        # Call the objects filtered by the user
        user_profiles = Profile.objects.filter(user=request.user)
        user_activities = Activity.objects.filter(user=request.user)
        user_nutritions = Nutrition.objects.filter(user=request.user)

        # Display attributes - if user has profiles (existing user)
        if user_profiles.exists():
            # Profile card
            user_last_profile = user_profiles.latest('updated_on')
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
            calories_burnt = user_last_activity.calories_burnt

            # Nutrition card
            user_last_nutrition = user_nutritions.latest('nutrition_on')
            food_item = user_last_nutrition.food_item
            portion = user_last_nutrition.portion
            protein = user_last_nutrition.protein
            carbs = user_last_nutrition.carbs
            fats = user_last_nutrition.fats
            calories_intake = user_last_nutrition.calories_intake

            # Metrics form
            metrics_form = MetricsForm()

            # If the user updates the values
            if request.method == "POST" and 'submitMetrics' in request.POST:
                metrics_form = MetricsForm(data=request.POST)

                # If user updates metrics form
                if metrics_form.is_valid() and username == request.user:
                    metrics = metrics_form.save(commit=False)
                    metrics.user_id = request.user.id
                    # get data from the form
                    metrics.weight = metrics_form.cleaned_data.get('weight')
                    metrics.weight_target = metrics_form.cleaned_data.get('weight_target')
                    weight, weight_target = metrics.weight, metrics.weight_target
                    metrics.height = user_last_profile.height
                    metrics.birthdate = user_last_profile.birthdate
                    metrics.profile_image = user_last_profile.profile_image

                    # commit changes
                    metrics.save() 
                    print('metrics form saved')

                    messages.add_message(
                        request, messages.SUCCESS,
                        'Your data has been updated!'
                        )
                    
                    return redirect('home')

            # Activity Form
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
                    activity.activity_type = request.POST.get('select-activity')
                    activity.duration = activity_form.cleaned_data.get('duration')
                    activity.distance = activity_form.cleaned_data.get('distance')

                    calories_burnt = get_calories_burnt(activity.activity_type, duration)

                    activity.calories_burnt = calories_burnt
                    activity_type, duration, distance = activity.activity_type, \
                                                        activity.duration, \
                                                        activity.distance

                    # commit changes
                    activity.save() 
                    print('activity form saved')

                    messages.add_message(
                        request, messages.SUCCESS,
                        'Your data has been updated!'
                        )

                    return redirect('home')

            # Nutrition Form
            nutrition_form = NutritionForm()

            # If the user updates the values
            if request.method == "POST" and 'submitNutrition' in request.POST:
                print('POST is executed')
                nutrition_form = NutritionForm(data=request.POST)

                # If user updates activity form
                if nutrition_form.is_valid() and username == request.user:
                    nutrition = nutrition_form.save(commit=False)
                    nutrition.user_id = request.user.id

                    # get data from the form
                    nutrition.food_item = nutrition_form.cleaned_data.get('food_item')
                    nutrition.portion = nutrition_form.cleaned_data.get('portion')

                    food_item = nutrition.food_item
                    portion = nutrition.portion

                    nutrition.calories_intake, nutrition.fats, \
                         nutrition.protein, nutrition.carbs = \
                         get_macronutrients(food_item, portion)

                    calories_intake, fats, protein, carbs = \
                        nutrition.calories_intake, nutrition.fats, \
                        nutrition.protein, nutrition.carbs

                    # commit changes
                    nutrition.save() 
                    print('nutrition form saved')

                    messages.add_message(
                        request, messages.SUCCESS,
                        'Your data has been updated!'
                        )

                    return redirect('home')
         

            # Profile Variables
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
                    'calories_burnt': calories_burnt,
                    'activity_form': activity_form,
                    'CAL_BURN_API_KEY': settings.CAL_BURN_API_KEY,
                    'food_item': food_item,
                    'portion': portion,
                    'protein': protein,
                    'carbs': carbs,
                    'fats': fats,
                    'calories_intake': calories_intake,
                    'nutrition_form': nutrition_form,
                    'GOOGLE_API_KEY': settings.GOOGLE_API_KEY,
                    'GOOGLE_CLIENT_ID': settings.GOOGLE_CLIENT_ID,
                })

        else:
            dict = entry_create(request)
            return render(
                request,
                "dashboard/entry_create.html",
                dict)

    else:
        return render(
            request,
            "dashboard/index.html",
        )


def profile_details(request):
    """
    Display an individual :model:`dashboard.Nutrition`.

    **Context**

    ``profile``
        An instance of :model:`dashboard.Nutrition`.

    **Template:**

    :template:`dashboard/profile_details.html`
    """

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
            weight_target = user_last_profile.weight_target
            profile_image = user_last_profile.profile_image

            # plotting
            all_objects = user_profiles.order_by('updated_on')

            time, weights = [], []
            for i in all_objects:
                time.append(i.updated_on)
                weights.append(i.weight)

            graph = plot_graph(time, weights, "Weight (Kg)", figsize=(14,6))

            # Profile form
            profile_form = ProfileForm()

            # If the user updates the values
            if request.method == "POST":
                profile_form = ProfileForm(data=request.POST, files=request.FILES)

                if profile_form.is_valid() and username == request.user:
                    profile = profile_form.save(commit=False)

                    profile.user_id = request.user.id
                    # get data from the form
                    profile.height = profile_form.cleaned_data.get('height')
                    profile.birthdate = profile_form.cleaned_data.get('birthdate')
                    profile.weight, profile.weight_target  = weight, weight_target

                    # if user updates picture use new one if not keep the last one
                    try:
                        if 'placeholder' in profile.profile_image.url:
                            profile.profile_image = user_last_profile.profile_image
                        else:
                            profile.profile_image = profile_form.cleaned_data.get('profile_image')
                    except:
                        profile.profile_image = profile_form.cleaned_data.get('profile_image')

                    profile_image = profile.profile_image

                    age = (date.today() - profile.birthdate) // timedelta(days=365.2425)
                    height = profile.height
                    birthdate = profile.height

                    # commit changes
                    profile.save() 
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
                    'graph': graph,
                    'height': height,
                    'weight': weight,
                    'age': age,
                    'profile_image': profile_image,
                    'profile_form': profile_form,
                    'birthdate': birthdate
                })
        
        else:
            dict = entry_create(request)
            return render(
                request,
                "dashboard/entry_create.html",
                dict)
    
    else:
        return render(
            request,
            "dashboard/index.html",
        )


def activity_history(request):
    """
    Display an individual :model:`dashboard.Nutrition`.

    **Context**

    ``profile``
        An instance of :model:`dashboard.Nutrition`.

    **Template:**

    :template:`dashboard/profile_details.html`
    """

    if request.user.is_authenticated:
        user_activities = Activity.objects.filter(user=request.user)
        user_profiles = Profile.objects.filter(user=request.user)

        # If user has profiles (existing user)
        if user_profiles.exists():
            user_last_activity =  user_activities.latest('activity_on')
            user_last_profile =  user_profiles.latest('updated_on')
            
            activity = user_last_activity.activity_type
            profile_image = user_last_profile.profile_image

            all_objects = user_activities.order_by('activity_on')

            time, calories_burnt = [], []
            for i in all_objects:
                time.append(i.activity_on)
                calories_burnt.append(i.calories_burnt)

            graph = plot_graph(time, calories_burnt, "Calories", figsize=(19,6))
        
            return render(
                request,
                "dashboard/activity.html",
                {
                    'graph': graph,
                    'activity': activity,
                    'profile_image': profile_image,
                })
        
        else:
            dict = entry_create(request)
            return render(
                request,
                "dashboard/entry_create.html",
                dict)
    
    else:
        return render(
            request,
            "dashboard/index.html",
        )


def nutrition_history(request):
    """
    Display an individual :model:`dashboard.Nutrition`.

    **Context**

    ``profile``
        An instance of :model:`dashboard.Nutrition`.

    **Template:**

    :template:`dashboard/profile_details.html`
    """

    if request.user.is_authenticated:
        user_nutritions = Nutrition.objects.filter(user=request.user)
        user_profiles = Profile.objects.filter(user=request.user)

        # If user has profiles (existing user)
        if user_profiles.exists():
            user_last_nutrition =  user_nutritions.latest('nutrition_on')
            user_last_profile =  user_profiles.latest('updated_on')
            
            food_item = user_last_nutrition.food_item
            profile_image = user_last_profile.profile_image

            all_objects = user_nutritions.order_by('nutrition_on')

            time, calories_intake = [], []
            for i in all_objects:
                time.append(i.nutrition_on)
                calories_intake.append(i.calories_intake)

            graph = plot_graph(time, calories_intake, "Calories", figsize=(19,6))
        
            return render(
                request,
                "dashboard/nutrition.html",
                {
                    'graph': graph,
                    'food_item': food_item,
                    'profile_image': profile_image,
                })
        
        else:
            dict = entry_create(request)
            return render(
                request,
                "dashboard/entry_create.html",
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

    if request.user.is_authenticated:
        user_profiles = Profile.objects.filter(user=request.user)

        if user_profiles.exists():
            user_last_profile =  user_profiles.latest('updated_on')
            profile_image = user_last_profile.profile_image

            return render(
                request,
                "dashboard/calendar.html",
                {   
                    'profile_image': profile_image,
                    'GOOGLE_API_KEY': settings.GOOGLE_API_KEY,
                    'GOOGLE_CLIENT_ID': settings.GOOGLE_CLIENT_ID,
                })

        else:
            dict = entry_create(request)
            return render(
                request,
                "dashboard/entry_create.html",
                dict)


def entry_create(request):
    """
    Display an individual :model:`dashboard.Nutrition`.

    **Context**

    ``profile``
        An instance of :model:`dashboard.Nutrition`.

    **Template:**

    :template:`dashboard/profile_details.html`
    """

    full_form = FullForm()
    height = age = weight = weight_target = profile_image = None

    if request.method == "POST":
        full_form = FullForm(data=request.POST)

        if full_form.is_valid():
            # Create Profile
            height = full_form.cleaned_data.get('height')
            weight = full_form.cleaned_data.get('weight')
            weight_target = full_form.cleaned_data.get('weight_target')
            birthdate = full_form.cleaned_data.get('birthdate')
            age = (date.today() - birthdate) // timedelta(days=365.2425)

            Profile.objects.create(user=request.user, height=height, weight=weight, 
                                birthdate=birthdate, weight_target=weight_target)

            # Create Activity
            activity_type = request.POST.get('select-activity')
            duration = full_form.cleaned_data.get('duration')
            distance = full_form.cleaned_data.get('distance')

            calories_burnt = get_calories_burnt(activity_type, duration)
            
            Activity.objects.create(user=request.user, activity_type=activity_type,
                                duration=duration, distance=distance,
                                calories_burnt = calories_burnt)

            # Create Nutrition
            food_item = full_form.cleaned_data.get('food_item')
            portion = full_form.cleaned_data.get('portion')

            calories_intake, fats, protein, carbs = \
                    get_macronutrients(food_item, portion)

            Nutrition.objects.create(user=request.user, food_item=food_item,
                                portion=portion, calories_intake=calories_intake,
                                fats=fats, protein=protein, carbs=carbs)

            print('full form saved')

            messages.add_message(
                request, messages.SUCCESS,
                'Your data has been created!'
            )

    dict = {
            'height': height,
            'weight': weight,
            'age': age,
            'profile_image': profile_image,
            'CAL_BURN_API_KEY': settings.CAL_BURN_API_KEY,
            'full_form': full_form,
            }

    return dict


def entry_delete(request):
    """
    Display an individual :model:`dashboard.Nutrition`.

    **Context**

    ``profile``
        An instance of :model:`dashboard.Nutrition`.

    **Template:**

    :template:`dashboard/profile_details.html`
    """
    
    request_url = request.build_absolute_uri()
    profiles = Profile.objects.filter(user=request.user)
    activities = Activity.objects.filter(user=request.user)
    nutritions = Nutrition.objects.filter(user=request.user)

    if 'profile' in request_url:
        if len(profiles) == 1:
            messages.add_message(request, messages.ERROR, 
                'You can not delete your first profile!')
        else:
            profiles.latest('updated_on').delete()
            messages.add_message(request, messages.SUCCESS,
                'Your last entry has been deleted!')
    if 'activity' in request_url:
        if len(activities) == 1:
            messages.add_message(request, messages.ERROR, 
                'You can not delete your first activity entry!')
        else:
            activities.latest('activity_on').delete()
            messages.add_message(request, messages.SUCCESS,
                'Your last entry has been deleted!')
    if 'nutrition' in request_url:
        if len(nutritions) == 1:
            messages.add_message(request, messages.ERROR, 
            'You can not delete your first nutrition entry!')
        else:
            nutritions.latest('nutrition_on').delete()
            messages.add_message(request, messages.SUCCESS,
                'Your last entry has been deleted!')             

    return HttpResponseRedirect(reverse('home'))


def plot_graph(x, y, ylabel, **kwargs):
    """
    Plot the graphs for tracking values with time
    """
    # plt.style.use('static/python/custom.mplstyle')
    plt.style.use('cyberpunk')

    fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True, **kwargs)

    ax.plot(x,y, marker="x", linewidth=3, markersize=12)
    mplcyberpunk.make_lines_glow()
    mplcyberpunk.add_gradient_fill(alpha_gradientglow=0.5, gradient_start='zero')        

    ax.tick_params(axis='x', labelrotation=60)
    ax.set_xlabel('Time', fontsize=18)
    ax.set_ylabel(ylabel, fontsize=18)
    ax.grid()

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg', bbox_inches='tight', dpi=100)
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data


def get_metrics(height, weight, birthdate):
    """
    Calculate Metrics to display on the dashboard
    """

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
        

def get_calories_burnt(activity, duration):
    """
    Fetch API to get caloroies for a certain activity and duration
    """

    api_url = f'https://api.api-ninjas.com/v1/caloriesburned?activity={activity}'
    response = requests.get(api_url, headers={'X-Api-Key': settings.CAL_BURN_API_KEY})
    if response.status_code == requests.codes.ok:
        activity = response.json()
        calories_burnt = activity[0]['total_calories'] * duration / 60
    else:
        print("Error:", response.status_code, response.text)

    return calories_burnt



def get_macronutrients(food, serving):
    """
    Fetch API to get caloroies for a certain food and serving
    """

    api_url = f'https://api.api-ninjas.com/v1/nutrition?query={serving}g {food}'
    response = requests.get(api_url, headers={'X-Api-Key': settings.CAL_BURN_API_KEY})
    if response.status_code == requests.codes.ok:
        macronutrients = response.json()[0]
        calories_intake = macronutrients['calories']
        fats = macronutrients['fat_total_g']
        protein = macronutrients['protein_g']
        carbs = macronutrients['carbohydrates_total_g']
    else:
        print("Error:", response.status_code, response.text)

    return calories_intake, fats, protein, carbs