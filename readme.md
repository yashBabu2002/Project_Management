
# Project Management System (Django + DRF)

## Tech Stack Used

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: Custom JWT-based authentication
- **User Model**: Custom `CustomUser` with role-based field (`admin`, `manager`, `developer`)
- **API Docs**: Swagger via `drf-yasg`
- **Containerization**: Docker & Docker Compose

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-repo/project-management.git
cd project-management
```

### 2. Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up PostgreSQL using Docker
```bash
docker-compose up --build
```

### 5. Run migrations and create superuser
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### 6. Load dummy data (optional)
```bash
docker-compose exec web python manage.py loaddata data.json
```

### 7. Access the app
- Swagger docs: http://localhost:8000/swagger/
- Admin Panel: http://localhost:8000/admin/

---

## Architecture Decisions

- **Custom User Model**:
  - Extended from `AbstractUser`.
  - Includes a `role` field to define user type (`admin`, `manager`, or `developer`).
  - No use of Django's `Groups` or `Permissions` model for roles — handled manually via the `role` attribute.

- **Registration Logic**:
  - Implemented in `RegisterView` and `RegisterSerializer`.
  - Validates password match.
  - Saves the user with the selected role from the request.

- **User Roles**:
  - Admin: Has full access.
  - Manager: Can manage projects and tasks.
  - Developer: Can be assigned tasks.

- **Modular Django Apps**:
  - `authentication`: Handles user registration and role assignment.
  - `project`: Manages projects and tasks.

---

## Dummy Data (Fixture Example)

Example `dummy_data.json` used for `loaddata`:

```json
[
  {
    "model": "authentication.customuser",
    "pk": 1,
    "fields": {
      "username": "adminuser",
      "email": "admin@example.com",
      "password": "pbkdf2_sha256$...$...",
      "is_active": true,
      "is_staff": true,
      "is_superuser": true,
      "role": "admin"
    }
  },
  {
    "model": "authentication.customuser",
    "pk": 2,
    "fields": {
      "username": "manager1",
      "email": "manager@example.com",
      "password": "pbkdf2_sha256$...$...",
      "is_active": true,
      "role": "manager"
    }
  },
  {
    "model": "authentication.customuser",
    "pk": 3,
    "fields": {
      "username": "dev1",
      "email": "dev@example.com",
      "password": "pbkdf2_sha256$...$...",
      "is_active": true,
      "role": "developer"
    }
  }
]
```

---

