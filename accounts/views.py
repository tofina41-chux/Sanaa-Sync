from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import HubSignUpForm, UserUpdateForm  # Import the new form
from resources.models import GigApplication

@login_required
def profile_view(request):
    # Fetch applications with status included
    my_applications = GigApplication.objects.filter(artist=request.user).select_related('gig')
    return render(request, 'accounts/profile.html', {'applications': my_applications})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile') # Redirect back to the dashboard
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'accounts/edit_profile.html', {'form': form})


# --- 1. The Landing Page (The "Artist Showcase") ---
def landing_page(request):
    # Only show artists who have been "Vetted" by the Hub Admin
    vetted_artists = User.objects.filter(role='creative', is_vetted=True).prefetch_related('skills')
    
    context = {
        'artists': vetted_artists,
        'page_title': "Sanaa-Sync | Creative Directory"
    }
    return render(request, 'accounts/landing.html', context)

# --- 2. The Signup Logic (The "Join the Hub" Action) ---
def signup(request):
    if request.method == 'POST':
        # Use HubSignUpForm so Django knows how to handle your custom User fields
        form = HubSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'creative'  # Ensure they start as a Creative
            user.save()
            
            # Log them in automatically so they don't have to sign in again immediately
            login(request, user)  
            
            return redirect('landing_page') 
    else:
        form = HubSignUpForm()
    
    return render(request, 'accounts/signup.html', {'form': form})
