# 🚑 Ambulance Tracking System

A full-stack Django web application designed to help users quickly locate, view, and book ambulances in emergency situations. The system provides location-based ambulance discovery, interactive map visualization, booking management, and administrative controls through Django Admin.

---

## 🌟 Features

### 👤 User Authentication

* User Registration
* User Login & Logout
* Secure Session Management
* Protected Booking Functionality

### 🚑 Ambulance Management

* View Available Ambulances
* Ambulance Details

  * Vehicle Number
  * Driver Name
  * Ambulance Type
  * Availability Status

### 📍 Nearest Ambulance Finder

* Browser Geolocation Integration
* Distance Calculation using Haversine Formula
* Sorts Ambulances by Proximity
* Helps users find the nearest available ambulance quickly

### 🗺️ Interactive Ambulance Map

* Built using Leaflet.js and OpenStreetMap
* Displays Ambulance Locations
* Displays User Location
* Interactive Markers and Popups

### 📋 Booking System

* Book an Ambulance
* Specify Pickup Location
* Specify Destination
* Add Emergency Description
* View Personal Booking History

### 📊 Dashboard

* Total Ambulances
* Available Ambulances
* Booked Ambulances
* Total Bookings

### 🔧 Admin Panel

* Manage Ambulances
* Manage Users
* Manage Bookings
* Update Booking Statuses

---

## 🏗️ Tech Stack

### Backend

* Python
* Django

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

### Database

* SQLite

### Maps & Location

* Leaflet.js
* OpenStreetMap
* Browser Geolocation API

### Deployment

* Render

### Version Control

* Git
* GitHub

---

## 📁 Project Structure

```text
ambulance_tracker/
│
├── accounts/          # Authentication & Registration
├── ambulance/         # Ambulance Management & Tracking
├── booking/           # Booking Functionality
├── config/            # Django Configuration
├── static/            # CSS & Static Assets
├── templates/         # HTML Templates
│
├── manage.py
├── requirements.txt
└── build.sh
```

---

## 🔄 Application Workflow

```text
User
  ↓
Register / Login
  ↓
View Available Ambulances
  ↓
Find Nearest Ambulance
  ↓
View Ambulance Locations on Map
  ↓
Book Ambulance
  ↓
Track Booking Status
```

---

## 📍 Nearest Ambulance Algorithm

The application uses the **Haversine Formula** to calculate the distance between:

* User's Current Location
* Ambulance Location

This ensures accurate distance calculations based on latitude and longitude coordinates.

```text
User Coordinates
        ↓
Available Ambulances
        ↓
Distance Calculation
        ↓
Sorting
        ↓
Nearest Ambulance First
```

---

## 🗺️ Map Integration

The system uses:

* **Leaflet.js** for interactive map rendering
* **OpenStreetMap** for free map tiles and geographic data

Features:

* Live User Location Display
* Ambulance Location Markers
* Interactive Popups
* Zoom & Navigation Controls

---

## 🚀 Local Setup

### Clone Repository

```bash
git clone https://github.com/WildTrio/ambulance-tracking-system.git
cd ambulance-tracking-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Linux / macOS

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py migrate
```

### Start Development Server

```bash
python manage.py runserver
```

Visit:

```text
http://127.0.0.1:8000
```

---

## 🔐 Admin Access

Create a superuser:

```bash
python manage.py createsuperuser
```

Run server and access:

```text
http://127.0.0.1:8000/admin/
```

---

## 🔮 Future Enhancements

* Real-Time GPS Tracking
* Live Ambulance Movement Updates
* AI-Based Emergency Severity Analysis
* Route Optimization Using Traffic Data
* SMS Notifications
* Email Notifications
* Hospital Integration
* PostgreSQL Database Support
* Mobile Application

---

## 🎯 Learning Outcomes

This project was developed as a practical exploration of:

* Django MVT Architecture
* Authentication & Authorization
* Django ORM
* Forms & Validation
* Database Relationships
* Geolocation APIs
* Map Integration
* Deployment on Render
* Git & GitHub Workflow

---

## 👨‍💻 Author

**Yash Patel**

Built as a full-stack Django project to explore location-based services, booking workflows, and real-world web application development.
