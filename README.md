# Daktari  Bora — Health Information Management Platform

## LIVE LINK TO WEBSITE -- https://daktari-bora-wv0m.onrender.com


![Daktari](https://github.com/user-attachments/assets/a64719f5-049e-4026-9775-0ef81044c304)


# 📊 Project Overview

Daktari bora is a full-stack health information management platform built using Django and HTML templates with Bootstrap 5 for responsive design. It allows doctors to manage client records, administer health programs, enroll clients into programs with status tracking, and expose secure APIs for external system integration.

This system is a technical challenge, showcasing backend and frontend development, clean coding, API-first design, relational database modeling, and basic security practices.



# 📃 Key Functionalities

-Create Health Programs (e.g., TB, Malaria, HIV)

-Register and manage Client profiles

-Enroll Clients into one or more Programs with status tracking (Active, Completed, Dropped)

-Search and View Client Profiles with enrolled Programs

-REST API exposure for client data retrieval

-Secure Authentication and Authorization

-Responsive Frontend using HTML templates and Bootstrap 5

-CORS support for API consumption



# 🏠 Project Structure

health_system/

├── accounts/ # Django app for authentication (Login/Logout)

├── clients/           # Django app for client registration and management

├── programs/          # Django app for health program management

├── templates/         # HTML templates for frontend rendering

├── health_system/     # Project settings, URLs, WSGI

├── manage.py          # Django management script

├── requirements.txt   # Python package requirements



# 🧰 System Architecture

Frontend: Django Templates + Bootstrap 5 (HTML/CSS)

Backend: Django 4.2 + Django REST Framework

Database: SQLite

Environment Management: Python Decouple

Authentication: Django SessionAuth

Deployment Readiness: Configured for Render


# 🚀 Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Ndungu-Jn/Daktari_bora/git
cd health_system
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables
Create a `.env` file:
```env
SECRET_KEY=your-django-secret-key
DEBUG=True
```

### 5. Apply Migrations
```bash
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Start Development Server
```bash
python manage.py runserver
```


# 📒 Usage Guide

- Login.
- Register if you have no account
- Add Programs via the Programs section
- Register Clients via the Clients section
- Enroll Clients into Programs
- View and search Clients
- View Client Profile with enrollment status

---

# 🔒 Security Considerations

- Sensitive configurations are managed via `.env`
- CORS allowed only in DEBUG mode
- CSRF protection active
- Authentication required for access
- Password validation enabled

---


**Developed by John Ndungu**
















