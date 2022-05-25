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
    "april": "Learn React for at least 20 minutes daily",
    "may": "Learn a new framework",
    "june": "Apply for a new Job",
    "july": "Apply Harder",
    "august": "Start Preparing to become a team lead",
    "september": "Organize Hackathon Within Your Team",
    "october": "Link up with people like mad",
    "november": "You are about to make it",
    "december": None
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

    return render(request, "challenges/index.html", {
        "challenge_month": months
    })


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
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
