# URL Shortener API

A simple and efficient URL shortener service built using Flask. This service allows users to shorten URLs and retrieve access count statistics for the shortened URLs. The system also includes an expiration mechanism for the generated short URLs.

## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [API Endpoints](#api-endpoints)
  - [POST /api/shorten](#post-apishorten)
  - [GET /api/r/<short_key>](#get-apirshort_key)
  - [GET /api/access-count/<short_key>](#get-apiaccess-countshort_key)
- [Project Setup](#project-setup)
  - [Prerequisites](#prerequisites)
  - [Running the Application](#running-the-application)
  - [Testing the Application](#testing-the-application)

## Introduction

The **URL Shortener API** is designed to convert long URLs into short, user-friendly links. This service provides an easy-to-use interface for shortening URLs and also tracks the access count for each shortened link. The service ensures that URLs are valid and provides an expiration mechanism for short links, which automatically cleans up expired URLs.

## Technologies Used

- **Flask** for building the REST API.
- **Flask-RESTful** for API routing.
- **Swagger (Flasgger)** for API documentation.
- **SQLite** for lightweight storage.
- **Python** for programming logic.

## Features

- **URL Shortening:** Convert long URLs into short, shareable links.
- **Access Count Tracking:** Track how many times a shortened URL has been accessed.
- **Expiration Mechanism:** Automatically removes expired URLs after 24 hours.
- **Swagger Documentation:** Automatically generated interactive API documentation.

## API Endpoints

- **POST /api/shorten**: Shortens long URLs.
- **GET /api/r/<short_key>**: Redirects to the original URL.
- **GET /api/access-count/<short_key>**: Retrieves the access count of a shortened URL.

## Project Setup

To get the project up and running, follow these simple steps:

### Prerequisites

Before you begin setting up the application, make sure you have the following software installed:

- **Python 3.8+**: Install Python from [here](https://www.python.org/downloads/).
- **Pip**: Python's package manager, included with Python.

### Running the Application

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/url-shortener-flask.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd url-shortener-flask
    ```
3. **Create a virtual environment (optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
5. **Run the application**:
    ```bash
    python app.py
    ```

6. Once the application is running, you can access the Swagger API docs at `http://localhost:5000/apidocs/`.

## Testing the Application

To test the application, you can use tools like **Postman** or **Swagger UI**.

### 1. **Shorten a URL**

- **Endpoint:** `POST /api/shorten`
- **Description:** This endpoint takes a long URL and returns a shortened URL.
- **Request Body:**
    ```json
    {
      "long_url": "https://example.com"
    }
    ```
- **Response:**
    ```json
    {
      "short_url": "http://localhost:5000/api/r/abc123",
      "short_key": "abc123"
    }
    ```

### 2. **Redirect to the Original URL**

- **Endpoint:** `GET /api/r/<short_key>`
- **Description:** This endpoint redirects to the original URL associated with the given short key.
- **Example:**
    - Request: `GET http://localhost:5000/api/r/abc123`
    - Response: Redirects to `https://example.com`.

### 3. **Get the Access Count for a Shortened URL**

- **Endpoint:** `GET /api/access-count/<short_key>`
- **Description:** This endpoint retrieves the number of times the shortened URL has been accessed.
- **Response:**
    ```json
    {
      "short_key": "abc123",
      "access_count": 5
    }
    ```

---
