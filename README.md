# Placement Management System (PMS)

## Overview

The Placement Management System (PMS) is a web-based application developed using Django that helps streamline the campus placement process. The system allows students to register, manage their profiles, search and apply for jobs, while companies can register, post job opportunities, and manage applicants.

## Features

### Student Module

* Student Registration and Login
* Profile Management
* Search Available Jobs
* Apply for Jobs
* View Applied Jobs
* Track Application Status

### Company Module

* Company Registration and Login
* Company Dashboard
* Post New Jobs
* View Job Applicants
* Manage Recruitment Process

### Job Management

* Job Posting with Eligibility Criteria
* Job Location and Mode Details
* Application Tracking
* Student-Company Interaction

## Technology Stack

### Backend

* Python
* Django Framework

### Frontend

* HTML
* CSS

### Database

* SQLite3

## Project Structure

```text
Placement Management System
│
├── manage.py
├── miniproject/
├── pms_app/
├── templates/
├── static/
└── db.sqlite3
```

## Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/YaminiManchala/djangoproject.git
```

### Navigate to Project Directory

```bash
cd djangoproject
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install django
```

### Run Migrations

```bash
python manage.py migrate
```

### Start Development Server

```bash
python manage.py runserver
```

### Open in Browser

```text
http://127.0.0.1:8000/
```

## Future Enhancements

* Email Notifications
* Resume Upload Feature
* Placement Statistics Dashboard
* Admin Analytics Panel
* Company Verification System

## Author

Yamini Manchala

B.Tech Student

This project is developed for educational and learning purposes.
