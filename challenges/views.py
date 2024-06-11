from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "learn python, learn algorithms and data structures, learn django, and flask",
    "february": "maybe learn java? IDK YET",
    "march": "this is march",
    "april": "this is april",
    "may": "this is may",
    "june": "this is june",
    "july": "this is july",
    "august": "this is august",
    "september": "this is september",
    "november": "this is november",
    "december": "this is december",
    }

def home_page(request):
    return render(request, "challenges/index.html", {"name": "Stanley", "months": list(monthly_challenges.keys())})

def monthly_challenges_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("<h1>404 page not found, idiot</h1>")

def monthly_challenge(request, month):
    try:
        return render(request, "challenges/challenge.html", {"month": month, "description": monthly_challenges[month],})
    except:
        return render(request, "challenges/challenge.html", {"err": "404"})
