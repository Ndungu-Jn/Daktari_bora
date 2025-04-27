# Daktari  Bora — Health Information Management Platform

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















