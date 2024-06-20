from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from datetime import date, timedelta
import numpy as np
from .models import Activity, Profile
from .forms import MetricsForm

# Create your views here.

# def index(request):
#     return HttpResponse('Hi. I am working!')


def dashboard(request):
    """
    Display an individual :model:`dashboard.Activity`.

    **Context**

    ``activity``
        An instance of :model:`dashboard.Activity`.

    **Template:**

    :template:`dashboard/index.html`
    """

    if request.user.is_authenticated:

        # # activity = Activity.objects.all()
        # Update foreign key
        p = Profile.objects.get(pk=1)
        Profile.objects.all().update(user=p)

        queryset = Profile.objects.filter(user=request.user).latest('updated_on')

        # user = Profile.objects.get(user=request.user)
        weight = queryset.weight
        height = queryset.height
        birthdate = queryset.birthdate

        # If the user updates the values
        metrics_form = MetricsForm()

        if request.method == "POST":
            metrics_form = MetricsForm(data=request.POST)

            if metrics_form.is_valid():
                # profile = metrics_form.save(commit=False)
                weight = metrics_form.cleaned_data.get('weight')
                height = metrics_form.cleaned_data.get('height')
                birthdate = metrics_form.cleaned_data.get('birthdate')

                profile = Profile(height=height, weight=weight, birthdate=birthdate)
                print('form is valid')
                profile.save()

                messages.add_message(
                    request, messages.SUCCESS,
                    'Your values have been updated!'
                    )

        # Body Mass Index (BMI)
        bmi_unrounded = weight / (height/100)**2    # kg/m2
        bmi = np.round(bmi_unrounded, 2)

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

        # Age
        age = (date.today() - birthdate) // timedelta(days=365.2425)
        
        # Basal Metabolic Rate (BMR)
        # Revised Harris-Benedict Equation (for Men - just for illustration)
        bmr = np.round(13.397 * weight + 4.799 * height - 5.677 * age + 88.362)

        rec_bmi = 24
        rec_weight =  np.round(rec_bmi * (height/100)**2, 1)

        # target_weight = 


        return render(
            request,
            "dashboard/index.html",
            {
                'bmi': bmi,
                'bmr': bmr,
                'classification': classification,
                'weight': weight,
                'height': height,
                'age': age,
                'metrics_form': metrics_form,
                'rec_bmi': rec_bmi,
                'rec_weight': rec_weight,
            }
        )
    
    else:
        return render(
            request,
            "dashboard/index.html",
        )