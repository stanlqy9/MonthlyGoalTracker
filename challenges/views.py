from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "<h1>learn python, learn algorithms and data structures, learn django, and flask<h1>",
    "february": "<h1>maybe learn java? IDK YET<h1>",
    "march": "<h1>march<h1>",
    "april": "<h1>this is april<h1>",
    "may": "may",
    "june": "june",
    "july": "july",
    "august": "august",
    "september": "september",
    "november": "november",
    "december": "december",
    }

def home_page(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href= '{month_path}'>{capitalized_month}</a></li>"
    list_items = f"<ul>{list_items}</ul>"
    return HttpResponse(list_items)

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
        return HttpResponse(monthly_challenges[month])
    except:
        return HttpResponseNotFound("<h1>404 page not found, idiot</h1>")

def practice_file(request):
    data = render_to_string("challenges/challenge.html")
    return HttpResponse(data)
