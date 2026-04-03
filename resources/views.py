from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Gig, GigApplication

def gig_list(request):
    # Only show gigs that are currently open for applications
    active_gigs = Gig.objects.filter(is_open=True).order_by('event_date')
    return render(request, 'resources/gig_list.html', {'gigs': active_gigs})

@login_required # Only logged-in artists can apply
def apply_for_gig(request, gig_id):
    gig = get_object_or_404(Gig, id=gig_id)
    
    if request.method == 'POST':
        # Create the application linked to the logged-in user
        GigApplication.objects.create(
            gig=gig,
            artist=request.user,
            message=request.POST.get('message', '')
        )
        return redirect('gig_list')
    
    return render(request, 'resources/apply_confirm.html', {'gig': gig})