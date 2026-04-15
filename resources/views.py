from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Added for user feedback
from .models import Gig, GigApplication, Resource, Booking
from .forms import BookingForm, GigApplicationForm

def gig_list(request):
    # Only show gigs that are currently open for applications
    active_gigs = Gig.objects.filter(is_open=True).order_by('event_date')
    return render(request, 'resources/gig_list.html', {'gigs': active_gigs})

@login_required # Only logged-in artists can apply
def apply_for_gig(request, gig_id):
    gig = get_object_or_404(Gig, id=gig_id)
    
    if request.method == 'POST':
        if not request.user.is_vetted:
            messages.warning(request, f"Access Denied. Your profile must be vetted to apply for '{gig.title}'. Please contact an administrator to get vetted.")
            return redirect('gig_list')
        
        form = GigApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Check if they already applied to prevent double submissions
            already_applied = GigApplication.objects.filter(gig=gig, artist=request.user).exists()
            
            if already_applied:
                messages.info(request, "You have already submitted an application for this gig.")
                return redirect('profile')

            # Create the application
            application = form.save(commit=False)
            application.gig = gig
            application.artist = request.user
            
            application.save()
            
            messages.success(request, f"Success! Your application for {gig.title} has been sent.")
            return redirect('profile') # Redirect to profile to see the application status
        else:
            messages.error(request, "Please provide either a text message or a voice recording.")
    else:
        form = GigApplicationForm()
    
    context = {'gig': gig, 'form': form}
    if not request.user.is_vetted:
        context['not_vetted'] = True
    
    return render(request, 'resources/apply_confirm.html', context)

def resource_list(request):
    """View available spaces, equipment, and instruments."""
    resources = Resource.objects.filter(status='available')
    return render(request, 'resources/resource_list.html', {'resources': resources})

@login_required
def book_resource(request, resource_id):
    """Handle booking of a specific resource."""
    resource = get_object_or_404(Resource, id=resource_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.resource = resource
            
            if booking.start_time >= booking.end_time:
                messages.error(request, "End time must be after start time.")
            else:
                # Check for overlapping bookings
                overlapping = Booking.objects.filter(
                    resource=resource,
                    status__in=['pending', 'approved'],
                    start_time__lt=booking.end_time,
                    end_time__gt=booking.start_time
                ).exists()
                
                if overlapping:
                    messages.error(request, "This resource is already booked for the selected time.")
                else:
                    booking.save()
                    messages.success(request, f"Your booking for {resource.name} is submitted and pending approval.")
                    return redirect('resource_list')
    else:
        form = BookingForm()
        
    return render(request, 'resources/booking_form.html', {'form': form, 'resource': resource})