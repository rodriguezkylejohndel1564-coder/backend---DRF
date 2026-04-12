# Backend Service

This directory contains the Django + Django REST Framework backend for the project.

## Location

Place this directory as `backend/` inside your main repository so it sits alongside the frontend and other services.

## Setup

1. Open PowerShell in `c:\Users\kylef\backend---DRF\backend`
2. Create a virtual environment:
   ```powershell
   python -m venv .venv
   ```
3. Activate the virtual environment:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   If PowerShell blocks execution, run:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\.venv\Scripts\Activate.ps1
   ```
4. Install project dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
5. Run database migrations:
   ```powershell
   python manage.py migrate
   ```
6. Start the development server:
   ```powershell
   python manage.py runserver
   ```

The backend server will be available at:

```text
http://127.0.0.1:8000/
```

## API Tutorial

### 1. Register a user

Request:

```http
POST /api/register/ HTTP/1.1
Host: 127.0.0.1:8000
Content-Type: application/json

{
  "username": "alice",
  "email": "alice@example.com",
  "password": "password123"
}
```

Response:

```json
{
  "user": {
    "id": 1,
    "username": "alice",
    "email": "alice@example.com"
  },
  "token": "<your-token>"
}
```

### 2. Login with the user

Request:

```http
POST /api/login/ HTTP/1.1
Host: 127.0.0.1:8000
Content-Type: application/json

{
  "username": "alice",
  "password": "password123"
}
```

Response:

```json
{
  "user": {
    "id": 1,
    "username": "alice",
    "email": "alice@example.com"
  },
  "token": "<your-token>"
}
```

### 3. Use the token for authenticated requests

For protected endpoints, add this header:

```http
Authorization: Token <your-token>
```

### 4. List products

Request:

```http
GET /api/products/ HTTP/1.1
Host: 127.0.0.1:8000
Authorization: Token <your-token>
```

### 5. Create a product

Request:

```http
POST /api/products/ HTTP/1.1
Host: 127.0.0.1:8000
Content-Type: application/json
Authorization: Token <your-token>

{
  "name": "Sample Product",
  "description": "A demo product",
  "price": "19.99"
}
```

Response:

```json
{
  "id": 1,
  "name": "Sample Product",
  "description": "A demo product",
  "price": "19.99",
  "created_by": {
    "id": 1,
    "username": "alice",
    "email": "alice@example.com"
  },
  "created_at": "2026-04-13T00:00:00Z"
}
```

## Example curl commands

Register:

```bash
curl -X POST http://127.0.0.1:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "alice", "email": "alice@example.com", "password": "password123"}'
```

Login:

```bash
curl -X POST http://127.0.0.1:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "alice", "password": "password123"}'
```

Create product:

```bash
curl -X POST http://127.0.0.1:8000/api/products/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token <your-token>" \
  -d '{"name": "Sample Product", "description": "A demo product", "price": "19.99"}'
```

## API Endpoints

- `POST /api/register/` - register a new user
- `POST /api/login/` - login and receive a token
- `GET /api/products/` - list products (requires token auth)
- `POST /api/products/` - create a product (requires token auth)

## Notes

- The backend uses token authentication with Django REST Framework.
- Use `backend/` as the working directory for all backend commands when this folder is inside a monorepo.
