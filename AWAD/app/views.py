"""
Definition of views.
"""

from django.shortcuts import render, redirect
from urllib import request
from app.forms import LogForm
from datetime import datetime
from .models import LogMessage, Film, Watchlist
import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required



@login_required
def add_to_watchlist(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    watchlist, created = Watchlist.objects.get_or_create(user=request.user, film=film)
    if created:
        # Optional: Add a message indicating success
        print(f"{film.title} added to your watchlist.")
    return redirect('film_reviews', film_id=film_id)

@login_required
def remove_from_watchlist(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    watchlist = Watchlist.objects.filter(user=request.user, film=film).first()
    if watchlist:
        watchlist.delete()
        # Optional: Add a message indicating removal
        print(f"{film.title} removed from your watchlist.")
    return redirect('film_reviews', film_id=film_id)

@login_required
def view_watchlist(request):
    watchlist = Watchlist.objects.filter(user=request.user)
    films = [item.film for item in watchlist]
    return render(request, 'watchlist.html', {'films': films})


def film_reviews(request, film_id):
    # Fetch the film details based on the provided film_id
    film = get_object_or_404(Film, id=film_id)
    # Fetch all LogMessages related to the film
    log_messages = LogMessage.objects.filter(title=film.title).order_by('-log_date')

    # Check if the film is in the user's watchlist
    in_watchlist = False
    if request.user.is_authenticated:
        in_watchlist = Watchlist.objects.filter(user=request.user, film=film).exists()

    return render(request, 'filmreviews.html', {
        'film': film,
        'log_messages': log_messages,
        'in_watchlist': in_watchlist
    })



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def set_cookie(request):
    response = redirect('home')
    response.set_cookie("review_cookie","reviews_cookiejar")
    return render(request, 'cookie.html')

def show_template(request):
    return render(request, 'cookie.html')



def sortReviews(request):
    # Get the sort option from the GET request; default to sorting by date
    sort_option = request.GET.get('sort', 'date')

    # Determine the sorting order based on the sort option
    if sort_option == 'title':
        messages = LogMessage.objects.order_by('title')
    elif sort_option == 'rating':
        messages = LogMessage.objects.order_by('rating')
    else:
        messages = LogMessage.objects.order_by('-log_date')

    # Pass the sorted messages and the selected sort option to the template
    return render(request, "reviewlist.html", {"message_list": messages, "sort_option": sort_option})



def editMessage(request, pk):
    message = get_object_or_404(LogMessage, pk=pk)
    if request.method == "POST":
        form = LogForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect("show")  # Redirect to the review list after saving
    else:
        form = LogForm(instance=message)  # Pre-populate the form with existing data

    return render(request, "edit.html", {"form": form, "message": message})


def deleteMessage(request, pk):
    message = get_object_or_404(LogMessage, pk=pk)  # Fetch the object by pk
    if request.method == "POST":
        message.delete()  # Delete the object
        return redirect("reviewlist")  # Redirect to the review list
    return render(request, "delete.html", {"message": message})  # Show confirmation page


def showMessages(request):
    messages = LogMessage.objects.order_by("-log_date")
    return render(request, "reviewlist.html", {"message_list": messages})


def addMessage(request):
    initial_data = {}
    if 'title' in request.GET:
        initial_data['title'] = request.GET['title']
    form = LogForm(request.POST or None, initial=initial_data)   
    if request.method == "POST" and form.is_valid():
        message = form.save(commit=False)
        message.log_date = datetime.now()
        message.save() # Save the review to the list
        return redirect("show")  # Show all reviews
    return render(request, "add.html", {"form": form})



def search(request):
    films = Film.objects.all()
    reviews = None
    if 'q' in request.GET and request.GET['q']:
        query = request.GET['q']
        films = films.filter(title__icontains=query)
        reviews = LogMessage.objects.filter(film__in=films)
    return render(request, 'search.html', {'films': films, 'reviews':reviews})

def searchAjax(request, q):
    filmsList = Film.objects.filter(title__icontains=q)
    return render(request, 'films.html', {'films': filmsList})



def home(request):
    films = Film.objects.all()  
    return render(request, 'home.html', {'films': films})






