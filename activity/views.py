from django.shortcuts import render
from django.http import HttpResponse
from .models import Activity

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

    activity = Activity.objects.all()

    return render(
        request,
        "activity/index.html",
        {
            "activity": activity,
        }
    )