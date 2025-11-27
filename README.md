# URL Shortener with Analytics

A Python Flask web application that generates shortened URLs and tracks click analytics. The service uses PostgreSQL for persistent storage and is deployed on Render for public access. Built to strengthen full-stack development, REST API design, database integration, and cloud deployment skills.

## Current Features
* Create shortened URLs through RESTful POST endpoint (`/shorten`)
* Redirect users from short URL to original link with automatic click tracking
* Real-time analytics dashboard (`/stats`) showing click counts per URL
* React frontend for easy URL shortening and stats visualization
* Persistent cloud storage using PostgreSQL
* Production-ready deployment on Render with Gunicorn WSGI server
* Business intelligence capabilities for link performance tracking
* CORS-enabled API for cross-origin requests

## Planned Features
* Add user accounts and authentication
* Enhanced analytics (geographic data, referrer tracking, time-based trends)
* Custom short codes (let users choose their own)

## Tech Stack
Python | Flask | PostgreSQL | Gunicorn | Render | REST API | React | CORS | psycopg2 | HTTP | JSON

## Status
✅ **Live and Functional** – Full-stack application deployed on Render with working React frontend and PostgreSQL backend.

## What I Learned
* Building RESTful APIs with Flask and PostgreSQL integration
* Production deployment on Render with environment variables
* React frontend development and API communication
* Full-stack architecture: browser → server → database flow
* Business intelligence through click tracking analytics
