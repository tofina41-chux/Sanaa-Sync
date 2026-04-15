# Sanaa-Sync: Swahilipot Hub Creatives Management System
The Professional Pulse of Swahilipot Hub Creatives Department.

An integrated Resource & Talent Management Ecosystem designed to bridge the gap between creative passion and professional excellence.

## Vision & Progress
Talent Intelligence: A dynamic database tracking artist skills and vetted Success Stories to increase market value.

Automated Operations: A smart booking engine for Hub spaces (Mekatilili, Ali Mazrui, Amphitheatre) and equipment.

Curated Marketplace: A secure bridge for partners to post gigs, allowing artists to apply and track their professional growth in real-time.

## Functional Modules (Implemented & Active)
1. The Artist & Resource Registry
Dynamic Resource Catalog: Digital tracking for the Amphitheatre, Mekatilili Hall, Ali Mazrui Hall, and equipment (Drums, Guitars, Mics).

Unique Routing: Every resource is indexed with a unique slug for professional URL routing and SEO.

Success Stories: (New!) Highlighting artist milestones directly on the landing page to build credibility with partners.

2. Marketplace & Gigs (Collaborative Release)
The Application Loop: Artists can now apply for posted gigs with personalized messages.

Live Status Tracking: Real-time visibility into application states: Pending Approval, Accepted, or Declined.

Opportunity Push: Allows the Dept. Head to curate high-value opportunities for vetted artists.

3. Internal Operations
Digital Booking Workflow: Replaces verbal/email requests with a "Greenlight" system. Requests stay "Pending" until admin approval.

Media Handling: Integrated Pillow for server-side image processing of artist portfolios and success story assets.

## Technical Stack & Implementation
Backend: Django 6.0.3 (Python)

Database: MariaDB/MySQL (via XAMPP)

Frontend: Tailwind CSS (Professional Blue Aesthetic)

Key Libraries: * Pillow: Image processing and optimization.

Django-Environ: Secure environment variable management.

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
Clone the Repo: git clone https://github.com/[your-repo]/sanaa-sync.git

Setup Environment: python -m venv venv and source venv/Scripts/activate

Install Dependencies: pip install -r requirements.txt (Includes Pillow, Django, etc.)

Database Migration: * Ensure XAMPP MySQL is running.

python manage.py migrate

Run Server: python manage.py runserver

Lead Developer: Tofina

Collaborators: Nassoro (Marketplace Logic), Kim (Success Stories/UI), kevin(Bookings logic)
