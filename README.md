![React](https://img.shields.io/badge/Frontend-React-blue)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-green)
![Status](https://img.shields.io/badge/status-in%20progress-yellow)

Intelli Sprint

A full-stack web application for personal sprint planning, time tracking, and productivity analytics.

Overview

Intelli Sprint is designed to help users manage their personal weekly sprints, track time spent on tasks, and gain insights into productivity.

The application follows a modern full-stack architecture with a React frontend and a FastAPI backend, designed for scalability and clean separation of concerns.

System Architecture

Components

Frontend (React + Vite)
User interface for managing tasks, running timers, and viewing analytics.

Backend (FastAPI)
Handles business logic, APIs, and data processing.

Database (PostgreSQL) (planned)
Stores tasks, time entries, and sprint data.

Data Flow

1. User interacts with the React frontend

2. Frontend sends HTTP requests to FastAPI endpoints

3. Backend processes task, timer, and analytics logic

4. Data is stored/retrieved from the database

5. Results are returned and rendered in the UI

Project Structure

intelli-sprint/
├── frontend/        # React (Vite)
├── backend/         # FastAPI
├── docs/            # Architecture diagrams
└── README.md

Tech Stack

Frontend

* React

* Vite

* JavaScript

Backend

* FastAPI (Python)

Database (planned)

* PostgreSQL

Features

1. Weekly sprint planning (Thu → Wed)

2. Daily task management

3. Task-level timers

4. Time tracking and analytics

5. Scalable full-stack architecture

License

MIT License