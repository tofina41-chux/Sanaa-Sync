from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from .forms import HubSignUpForm, UserUpdateForm
from resources.models import GigApplication, SuccessStory, Resource

@login_required
def profile_view(request):
    # Fixed: changed 'created_at' to 'applied_on' to match your model
    my_applications = GigApplication.objects.filter(artist=request.user).select_related('gig').order_by('-applied_on')
    return render(request, 'accounts/profile.html', {'applications': my_applications})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile_view')
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'accounts/edit_profile.html', {'form': form})

# --- 1. The Landing Page (The "Artist Showcase") ---
def landing_page(request):
    # Fetch Success Stories (your milestones)
    success_stories = SuccessStory.objects.all().order_by('-created_at')
    
    # Fetch Equipment (Resource type 'gear' or 'instrument')
    equipment = Resource.objects.filter(
        resource_type__in=['gear', 'instrument'], 
        status='available'
    )[:6] # Limit to 6 so the page isn't too long
    
    # Fetch Halls (Resource type 'hall')
    halls = Resource.objects.filter(
        resource_type='hall', 
        status='available'
    )
    
    context = {
        'success_stories': success_stories,
        'equipment': equipment,
        'halls': halls,
        'page_title': 'Sanaa-Sync V2 | Home'
    }
    
    return render(request, 'accounts/landing.html', context)
# --- 2. The Success Story Detail Page ---
def story_detail(request, story_id):
    story = get_object_or_404(SuccessStory, pk=story_id)
    return render(request, 'accounts/story_detail.html', {'story': story, 'page_title': f"{story.artist_name} | Story Detail"})

# --- 3. The Signup Logic (The "Join the Hub" Action) ---
def signup(request):
    if request.method == 'POST':
        form = HubSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'creative'
            user.save()
             
            login(request, user)
            messages.info(request, "Welcome to Sanaa-Sync! Your account is currently under review.")
            return redirect('landing_page') 
    else:
        form = HubSignUpForm()
    
    return render(request, 'accounts/signup.html', {'form': form})