# Sanaa-Sync:  Swahilipot Hub Creatives Management System
Sanaa-Sync is a centralized platform for the Swahilipot Hub Creatives Department. It streamlines the connection between vetted artists and professional opportunities (Gigs) while providing a "Caesar Portal" for user profile management.

## Core Features
### Artist Vetting System: 
A custom User model with admin-controlled vetting (is_vetted) and activation statuses.

### Gig Management: 
Centralized resource tracking for opportunities, including budget, requirements, and event dates.

### Automated Notifications: 
Django Signals-based email system that alerts vetted artists the moment a new gig is posted.

### Talent Directory: 
A public-facing list of vetted creatives for external clients.

## Technical Stack

Framework: Django 6.0.3

Database: MariaDB (via XAMPP/MySQL)

Environment: Python 3.12+

Frontend: Bootstrap / Django Templates

## Notification Engine (Signals)
The project utilizes Django Signals to maintain a decoupled architecture:

  Location: accounts/signals.py

  Triggers:

  post_save (User): Sends a welcome email on signup and a "Verified" email when an admin vets the user.

post_save (Gig): Sends a broadcast email to all is_vetted=True users when a new open gig is created.

## File Structure (Current)

sanaa_sync/
├── manage.py
├── core/                  # Project Settings & Routing
├── apps/
│   ├── accounts/          # Custom User (Creative/Client), Roles, Profiles
│   ├── resources/         # Asset Management, Slugs, Booking Logic
│   ├── marketplace/       # Gigs, Applications, Status Tracking
│   └── operations/        # Success Stories, Media Assets
├── static/                # Tailwind CSS, Global Assets
├── templates/             # Professional Blue Swiss-Style UI
└── requirements.txt       # Project Dependencies
## Roadmap & Future AI Integration
Phase 3 (AI Layer): Integrating Gemini API for "Smart Match" gig recommendations and automated Artist Portfolio Enhancement.

Phase 4 (Scaling): Transitioning from distributed local XAMPP environments to a centralized Cloud Database (PostgreSQL/Supabase).

Phase 5 (Mobile): Progressive Web App (PWA) capabilities for on-the-go booking and gig alerts.

## Setup & Installation for Developers
Clone the Repo: 
  git clone https://github.com/[your-repo]/sanaa-sync.git

Setup Environment:
  python -m venv venv 
  source venv/Scripts/activate

Install Dependencies: 
  pip install -r requirements.txt (Includes Pillow, Django, etc.)

Database Migration: 
* Ensure XAMPP MySQL is running. Update core/settings.py with your local database credentials.

  python manage.py migrate

Run Server: 
  python manage.py runserver
  
## The "Sync" Migration (CRITICAL)
If your local DB is out of sync with the latest model changes:

  python manage.py migrate resources zero --fake
  python manage.py migrate resources --fake-initial
  python manage.py migrate

## Troubleshooting
  Duplicate Column Error: 
    Run python manage.py migrate <app_name> <last_working_migration> --fake to align the ledger.

  Signals Not Firing: 
    Check accounts/apps.py to ensure the ready() method imports the signals file.

  Emails Not Appearing: 
    In development, check the terminal console. Emails are routed to the console backend by default.

## Contribution Guidelines
  Always create a new branch for features: git checkout -b feature/your-feature.

  Never push migration files that haven't been tested against a clean database.
  
  
Lead Developer: Wafula(tofina41-chux)

Collaborators: Nassoro (Marketplace Logic), Kim (Success Stories/UI), kevin(Bookings logic)
