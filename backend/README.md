# Intelli Sprint – Backend Design
## Overview

This document describes the database design and backend structure for the Intelli Sprint application.

The backend is responsible for managing:

* Sprint planning (weekly structure)

* Activities (reusable units of work)

* Scheduling of activities within sprint weeks

The system is designed to be scalable, flexible, and analytics-ready.

## Design Principles

Separation of concerns: Activities, sprint weeks, and scheduling are modelled independently

Reusability: Activities can span multiple sprint weeks

Extensibility: Designed to support timers, analytics, and status tracking

Normalisation: Avoids duplication through relational modelling

## Database Schema

The database consists of three core tables:

activities
sprint_weeks
sprint_activities

## Table: activities

Represents reusable units of work that can be scheduled across multiple sprint weeks.

Columns

id (Integer, Primary Key)

name (String, required)

created_at (DateTime)

## Table: sprint_weeks

Represents a single sprint cycle (Thursday → Wednesday).

Columns

id (Integer, Primary Key)

week_start_date (Date, required) — typically a Thursday

semester_week (Integer, required) — user-defined week index

created_at (DateTime)

## Table: sprint_activities

Associates activities with sprint weeks.

This is a many-to-many relationship table with additional metadata.

Columns

id (Integer, Primary Key)

sprint_week_id (Foreign Key → sprint_weeks.id)

activity_id (Foreign Key → activities.id)

day (String, required) — e.g. Thu, Fri, Sat

status (String, optional) — planned, in-progress, completed

## Relationships
activities          sprint_activities          sprint_weeks
    |                     |                        |
    |---------------------|------------------------|
           many-to-many relationship

One activity can belong to multiple sprint weeks

One sprint week can contain multiple activities

The sprint_activities table manages this relationship

## Data Model Summary

Activity = reusable task

Sprint Week = time container

Sprint Activity = scheduling layer

## Future Extensions

This schema supports future features such as:

### Time Tracking
time_entries
- id
- sprint_activity_id
- start_time
- end_time
- duration

### Analytics

Time spent per activity

Time spent per sprint week

Productivity trends over time

### Status Tracking

planned

in-progress

completed

### Planned API Endpoints
POST /activities
POST /sprint-weeks
POST /sprint-weeks/{id}/activities
GET  /sprint-weeks/current

### Technology Stack

FastAPI – backend framework

SQLAlchemy – ORM

SQLite (initial) → PostgreSQL (future)

### Notes

SQLite is used for initial development

Schema is designed to transition easily to PostgreSQL

API layer will be built on top of this schema

### Next Steps

Implement SQLAlchemy models

Create database tables

Build API endpoints