from ast import arg
from http.client import responses
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# Create your views here.

monthly_challenge = {
    "january": "Eat no meat",
    "february": "Walk for at least 20 minute",
    "march": "Learn Django for at least 20 minutes daily",
    "april": "Learn Django for at least 20 minutes daily",
    "may": "Learn Django for at least 20 minutes daily",
    "june": "Learn Django for at least 20 minutes daily",
    "july": "Learn Django for at least 20 minutes daily",
    "august": "Learn Django for at least 20 minutes daily",
    "september": "Learn Django for at least 20 minutes daily",
    "october": "Learn Django for at least 20 minutes daily",
    "november": "Learn Django for at least 20 minutes daily",
    "december": "Learn Django for at least 20 minutes daily"
}

# def january(request):
#     return HttpResponse("Don't eat meat at all")


# def february(request):
#     return HttpResponse("Walk for at least 20 minutes everyday")


# def march(request):
#     return HttpResponse("Learn Django for at least 20 minutes daily")
def index(request):
    list_items = ""
    months = list(monthly_challenge.keys())

    for month in months:
        cap_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{cap_month}</a></li>"

    return HttpResponse(f"<ul>{list_items}</ul>")


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenge.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_months = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_months])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenge[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
