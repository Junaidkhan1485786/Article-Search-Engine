# Article-Search-Engine

# Indian Constitution Articles Web App

This is a web application built using **FastAPI**, **MySQL**, and **Uvicorn**. It allows users to register, log in, and view articles from the Indian Constitution in a structured and accessible format.

## Features

- User registration with secure password hashing and validation.
- Login functionality with redirection to the main page upon successful login.
- Main page displays all articles from the Indian Constitution.
- Front-end uses HTML and CSS for responsive design.

## Technology Stack

Backend: FastAPI (Python)  
Frontend: HTML, CSS  
Database: MySQL  
Server: Uvicorn  
Authentication: Custom login and registration system with hashed passwords  
ORM: SQLAlchemy (optional)  

## Project Structure

📦 myapp  
┣ 📂app  
┃ ┣ 📜main.py - Main FastAPI app file (routes and article handling)  
┃ ┣ 📜auth.py - User authentication (login, registration, session handling)  
┃ ┣ 📂templates - HTML templates for rendering pages  
┃ ┃ ┣ 📜index.html - Main page showing articles  
┃ ┃ ┣ 📜login.html - Login form page  
┃ ┃ ┣ 📜register.html - Registration form page  
┃ ┣ 📂static - Static files (CSS, JS)  
┃ ┣ 📂database - Database models and connection setup  
┃ ┣ 📜models.py - SQLAlchemy models for User and Articles  
┃ ┣ 📜crud.py - CRUD operations for interacting with the database  
┃ ┣ 📜config.py - Configuration for environment variables  
┣ 📜requirements.txt - List of dependencies  
┣ 📜README.md - This file  

## Installation and Setup Instructions

To set up and run this project locally, follow these steps:

1. Clone the Repository:  
`git clone https://github.com/yourusername/indian-constitution-app.git`  
`cd indian-constitution-app`

2. Create a Virtual Environment and Activate it:  
`python -m venv venv`  
`source venv/bin/activate` (On Windows use `venv\Scripts\activate`)

3. Install Dependencies:  
`pip install -r requirements.txt`

4. Set up MySQL Database:  
Ensure MySQL is installed and running. Create a database called `constitution_db`.  
Create a user with access:  
`CREATE DATABASE constitution_db;`  
`CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'password';`  
`GRANT ALL PRIVILEGES ON constitution_db.* TO 'appuser'@'localhost';`

5. Configure Environment Variables:  
Create a `.env` file in the root directory with the following content:  
`DB_NAME=constitution_db`  
`DB_USER=appuser`  
`DB_PASSWORD=password`  
`DB_HOST=localhost`  
`DB_PORT=3306`  
`SECRET_KEY=your-secret-key`

6. Apply Migrations (If Using SQLAlchemy):  
`alembic upgrade head`

7. Run the Application:  
`uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

8. Access the Application:  
Open a browser and go to `http://localhost:8000`

Enjoy reading the Indian Constitution articles!

