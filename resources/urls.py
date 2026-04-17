from django.urls import path
from . import views

urlpatterns = [
    # Gigs
    path('gigs/', views.gig_list, name='gig_list'), 
    path('gigs/apply/<int:gig_id>/', views.apply_for_gig, name='apply_for_gig'),
    
    # New Gallery views for the Navbar
    path('halls/', views.halls_list, name='halls_list'),
    path('equipment/', views.equipment_list, name='equipment_list'),
    
    # The new Master Booking Form (replaces individual book_resource)
    path('booking/', views.book_multiple, name='master_booking'),
]