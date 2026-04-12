# Backend Service

This directory contains the Django + Django REST Framework backend for the project.

## Location

Place this directory as `backend/` inside your main repository so it sits alongside the frontend and other services.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- `POST /api/register/` - register a new user
- `POST /api/login/` - login and receive a token
- `GET/POST /api/products/` - manage products (authenticated)

## Notes

- The backend uses token authentication with DRF.
- If added into a monorepo, use the `backend/` path as the working directory for backend commands.
