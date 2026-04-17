from django.contrib import admin
from .models import Resource, Booking, BookingItem, Gig, GigApplication, SuccessStory

# This allows us to add multiple resources to one booking in the admin panel
class BookingItemInline(admin.TabularInline):
    model = BookingItem
    extra = 1

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    # Added 'image' to see if a resource has a photo in the list view
    list_display = ('name', 'resource_type', 'status', 'quantity', 'capacity')
    list_filter = ('resource_type', 'status')
    search_fields = ('name', 'description')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    # REMOVED 'resource' from list_display because it's now in BookingItem
    list_display = ('event_title', 'user', 'start_time', 'end_time', 'status', 'assigned_staff')
    list_filter = ('status', 'start_time')
    date_hierarchy = 'start_time'
    inlines = [BookingItemInline] # This shows the multi-item form

# --- Marketplace Admin remains the same but with clean imports ---

class GigApplicationInline(admin.TabularInline):
    model = GigApplication
    extra = 0
    readonly_fields = ('applied_on',)

@admin.register(Gig)
class GigAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'location', 'slots_available', 'is_open', 'applicant_count')
    list_filter = ('is_open', 'event_date')
    search_fields = ('title', 'description')
    inlines = [GigApplicationInline]

    def applicant_count(self, obj):
        return obj.applications.count()
    applicant_count.short_description = "Applicants"

@admin.register(GigApplication)
class GigApplicationAdmin(admin.ModelAdmin):
    list_display = ('artist', 'gig', 'status', 'applied_on')
    list_filter = ('status', 'applied_on')
    # Note: ensure your User model has search_fields in its admin to use autocomplete
    # If it causes errors, just comment out autocomplete_fields below
    # autocomplete_fields = ['artist', 'gig'] 

@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ('artist_name', 'is_featured', 'created_at')
    list_filter = ('is_featured', 'created_at')
    search_fields = ('artist_name', 'story')