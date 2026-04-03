from django.contrib import admin
from django.urls import path, include

# Custom "Caesar" Admin Header Customization
admin.site.site_header = "Sanaa-Sync: Swahilipot Admin"
admin.site.site_title = "Caesar Portal"
admin.site.index_title = "Swahilipot Creatives Dept."

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),   # Home, Login, Signup
    path('', include('resources.urls')),  # This UNLOCKS the 'gig_list' and 'booking' logic
]