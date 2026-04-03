from django.urls import path
from . import views

urlpatterns = [
    # This 'name' must match exactly what you wrote in base.html
    path('gigs/', views.gig_list, name='gig_list'), 
    path('gigs/apply/<int:gig_id>/', views.apply_for_gig, name='apply_for_gig'),
]