# URL Shortener Microservice

A Python Flask web application that generates shortened URLs and tracks click analytics. The service uses PostgreSQL for persistent storage and is deployed on Render for public access. Built to strengthen backend development, REST API design, database integration, and cloud deployment skills.

## Current Features
- Create shortened URLs through RESTful POST endpoint (`/shorten`)
- Redirect users from short URL to original link with automatic click tracking
- Real-time analytics dashboard (`/stats`) showing click counts per URL
- Persistent cloud storage using PostgreSQL
- Production-ready deployment on Render with Gunicorn WSGI server
- Business intelligence capabilities for link performance tracking

## Planned Features
- Add user accounts and authentication
- Create web frontend for link submission and stats visualization (currently API-only)
- Enhanced analytics (geographic data, referrer tracking, time-based trends)
  
## Tech Stack
Python | Flask | PostgreSQL | Gunicorn | Render | REST API | psycopg2 | HTTP | JSON

## Status
In Progress – Core API fully functional and publicly accessible. Database migrated to PostgreSQL. Currently accessible via API endpoints (curl/Postman); web UI in development.

## What I’m Learning
- Building RESTful APIs with Flask and handling different HTTP methods
- Integrating PostgreSQL databases for persistent data storage
- Managing HTTP redirects and tracking user interactions
- Cloud deployment on Render with environment variables
- Understanding production web architecture (Gunicorn vs Flask dev server)
- Implementing basic business intelligence through click analytics
- Request flow from browser through multiple server layers to database
