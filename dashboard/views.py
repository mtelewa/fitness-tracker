from django.shortcuts import render
from django.http import HttpResponse
from .models import Activity, Profile
import numpy as np
from dateutil.relativedelta import relativedelta
import datetime

# Create your views here.

# def index(request):
#     return HttpResponse('Hi. I am working!')


def index(request):
    """
    Display an individual :model:`dashboard.Activity`.

    **Context**

    ``activity``
        An instance of :model:`dashboard.Activity`.

    **Template:**

    :template:`activity/index.html`
    """

    # activity = Activity.objects.all()

    user = Profile.objects.get(user=request.user)
    weight = user.weight
    height = user.height
    birthdate = user.birthdate

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
    today = datetime.date.today()
    age = relativedelta(today, birthdate).years
    
    # Basal Metabolic Rate (BMR)
    # Revised Harris-Benedict Equation (for Men - just for illustration)
    bmr = np.round(13.397 * weight + 4.799 * height - 5.677 * age + 88.362)

    return render(
        request,
        "dashboard/index.html",
        {
            'bmi': bmi,
            'classification': classification,
            'weight': weight,
            'height': height,
            'age': age,
            'bmr': bmr,
        }
    )