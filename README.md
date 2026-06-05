# RunBench — Real-Time Benchmarking Suite for Runware Models

## Overview

RunBench is a high-throughput benchmarking platform built for the Runware ecosystem. It helps developers compare AI models based on real-world performance metrics such as latency, throughput, cost, and reliability before deploying them into production workflows.

Instead of relying on assumptions, developers can stress-test multiple Runware models simultaneously and make data-driven decisions backed by live performance analytics.

---

## The Problem

Runware provides access to hundreds of powerful AI models, giving developers tremendous flexibility. However, choosing the right model for a production workload can be difficult.

Questions developers often face:

* Which model generates results the fastest?
* Which model offers the best cost-performance ratio?
* Which model remains stable under heavy traffic?
* How do different models compare in real-time?

Without a dedicated benchmarking system, answering these questions requires significant manual testing and analysis.

---

## The Solution

RunBench acts as a dedicated performance laboratory for Runware models.

The platform automatically:

* Executes parallel benchmark tests across multiple models
* Measures generation latency and throughput
* Tracks success and failure rates
* Calculates cost-per-generation metrics
* Stores benchmark data securely
* Visualizes performance in real time through an interactive dashboard

This enables developers to quickly identify the best model for their specific latency and budget requirements.

---

## Key Features

### High-Throughput Stress Testing

Launch concurrent benchmark jobs across multiple Runware models without blocking application performance.

### Real-Time Analytics Dashboard

Monitor live metrics including:

* Time to Image (TTI)
* Average latency
* Success rate
* Failure rate
* Cost per batch
* Request throughput

###  Secure Data Storage

Benchmark results are stored in Supabase with Row Level Security (RLS) enabled for secure access control.

### Decoupled Architecture

The benchmarking worker operates independently from the dashboard API, ensuring smooth performance even during heavy testing.

### Modern Glassmorphism UI

A clean and modern interface designed for effortless monitoring and comparison.

---

## Architecture

Frontend (Glassmorphism Dashboard)
↓
Flask REST API
↓
Async Benchmark Workers
↓
Runware Models
↓
Supabase Database (RLS Enabled)

---

## Tech Stack

### Backend

* Python
* Flask
* AsyncIO
* REST APIs

### Database

* Supabase
* PostgreSQL
* Row Level Security (RLS)

### Frontend

* HTML
* CSS
* JavaScript
* Glassmorphism Design System

### AI Infrastructure

* Runware API
* Multi-model Benchmarking Engine

---

## Challenges Solved

### Concurrency at Scale

Implemented asynchronous benchmarking workers capable of firing multiple requests simultaneously without affecting dashboard responsiveness.

### Unified Metric Standardization

Normalized performance data from different models into a consistent schema for easier analysis and comparison.

### Real-Time Visualization

Optimized frontend state management to render live benchmark updates efficiently and smoothly.

---

## Example Use Case

A developer needs an image generation model that:

* Responds in under 3 seconds
* Maintains a high success rate
* Fits within a fixed budget

Instead of manually testing every available model, RunBench automatically benchmarks available options and provides clear performance insights through a single dashboard.

---

## Future Improvements

* Historical benchmark trends
* Automated model ranking
* Team collaboration features
* Benchmark export reports
* Advanced cost prediction analytics
* Cross-region performance testing

---

## Author

**Manvith Balaji**

Built as a proof-of-concept to improve transparency, benchmarking, and model selection within the Runware ecosystem.
