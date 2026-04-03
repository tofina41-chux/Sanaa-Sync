from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import User, ArtistSkill
from .forms import HubSignUpForm  # <--- Crucial: Importing your custom form
from django.contrib.auth.decorators import login_required
from resources.models import GigApplication # Assuming this is where applications live

@login_required
def profile_view(request):
    # Fetch applications this specific artist has made
    my_applications = GigApplication.objects.filter(artist=request.user).select_related('gig')
    
    context = {
        'user': request.user,
        'applications': my_applications,
    }
    return render(request, 'accounts/profile.html', context)
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
