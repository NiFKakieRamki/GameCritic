from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('reviews:list')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form':form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('reviews:list')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('reviews:list')

def author_profile_view(request, username):

    User = get_user_model()

    author = get_object_or_404(User, username=username)

    author_reviews = author.reviews.filter(is_published=True).order_by('-created_at')

    context = {
        'author': author,
        'author_reviews': author_reviews
    }

    return render(request, 'users/author_profile.html', context)
