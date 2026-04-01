![React](https://img.shields.io/badge/Frontend-React-blue)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-green)
![Status](https://img.shields.io/badge/status-In%20progress-yellow)

# SprintAWeek

A full-stack web application for personal sprint planning, time tracking, productivity analytics and a motivation corner.

## Overview

SprintAWeek is designed to help users manage their personal weekly sprints, track time spent on tasks, and gain insights into productivity. A "time capsule" feature will allow users to send notes to themselves, which will be displayed in the "motivation corner" at a random day in the near future. The app is designed targeting university students and academics, but it would suit anyone working autonomously with a flexible schedule who wants to keep track of their activities and efficiency.

The application follows a modern full-stack architecture with a **React frontend (JavaScript)** and a **FastAPI backend (Python)**, designed for scalability and clean separation of concerns. The UI is desgined to be minimalistic to allow users to plan their sprints within minutes and easily keep track of their progress during the week.

## Features

1. Weekly sprint planning (Monday to Sunday)
2. Daily task management
3. Task-level timers
4. Time tracking and analytics
5. Time capsule feature for motivating the user

## System Architecture

### Components

* **Frontend (React + Vite)**: User interface for managing tasks, running timers, and viewing analytics.
* **Backend (FastAPI, SQLAlchemy)**: Handles business logic, APIs, and data processing.
* **Database (SQLite)**: Stores tasks, time entries, sprint data and time capsule notes.

### Data Flow

1. User interacts with the React frontend
2. Frontend sends HTTP requests to FastAPI endpoints
3. Backend processes task, timer, and analytics logic
4. Data is stored/retrieved from the database
5. Results are returned and rendered in the UI

## Tech Stack

### Frontend

* React
* Vite
* JavaScript

### Backend

* FastAPI (Python)
* SQLAlchemy (ORM)

### Database

* SQLite

## License

MIT License