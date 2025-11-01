# URL Shortener Microservice

A Python Flask application that generates and resolves shortened URLs. The service stores mappings between original and shortened URLs in a local SQLite database and tracks how many times each link is used. Designed to strengthen backend development skills, REST API design, and database integration.

## Current Features
- Create and retrieve shortened URLs through RESTful endpoints
- Redirect users from short URL to original link
- Persistent data storage using SQLite (`urls.db`)
- Basic click counter for usage analytics

## Planned Features
- Migrate database from SQLite to PostgreSQL for scalability
- Add user accounts and authentication
- Deploy on Render or AWS Lambda for public access
- Create simple web frontend for link submission and stats display

## Tech Stack
Python | Flask | SQLite | REST API | HTTP | JSON

## Status
In Progress – Core API and database fully functional; migration and deployment planned.

## What I’m Learning
Building RESTful APIs with Flask, integrating databases for persistence, managing HTTP redirects, and preparing applications for cloud deployment.
