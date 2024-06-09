from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "learn python, learn algorithms and data structures, learn django, and flask",
    "february": "maybe learn java? IDK YET",
    "march": "march",
    "april": "this is april",
}

def home_page(request):
    return HttpResponse("<ul><li>January</li><li>February</li></ul>")

def monthly_challenges_by_number(request, month):
    try:
        requested_month = list(monthly_challenges.keys())[month - 1]
        return HttpResponseRedirect("/" + requested_month)
    except:
        return HttpResponseNotFound("<h1>404 page not found, idiot</h1>")

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("<h1>404 page not found, idiot</h1>")

