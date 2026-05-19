# CloudShare – Cloud File Sharing Application

## Introduction

CloudShare is a cloud-based file sharing web application developed using Flask. The project allows users to create an account, log in, upload files, download files, and manage uploaded content through a simple web interface.

This project was developed during my internship to learn practical concepts related to cloud computing, Linux server management, Docker, AWS services, and deployment of web applications.

---

## Features

- User Registration and Login
- Password Hashing
- File Upload and Download
- Delete Uploaded Files
- Dark and Light Theme
- Responsive User Interface
- Docker Support
- AWS EC2 Deployment
- AWS S3 Backup Storage
- GitHub Actions CI/CD Workflow
- CloudWatch Monitoring

---

## Technologies Used

### Frontend
- HTML
- CSS
- Bootstrap
- JavaScript

### Backend
- Python
- Flask
- Flask-SQLAlchemy

### Cloud and DevOps
- AWS EC2
- AWS S3
- AWS CloudWatch
- Docker
- Nginx
- Gunicorn
- GitHub Actions

---

## Project Working

The application is deployed on an AWS EC2 Ubuntu server. Nginx is used as a reverse proxy server, and Gunicorn is used to run the Flask application. Docker is used for containerization, and GitHub Actions is used for basic CI/CD automation.

Uploaded files and database backups are stored in AWS S3 for backup purposes. CloudWatch is used to monitor the EC2 instance and CPU usage.

---

## Architecture

User Browser
↓
Nginx
↓
Docker Container
↓
Gunicorn
↓
Flask Application
↓
SQLite Database

Additional AWS Services:
- Amazon S3 for backups
- CloudWatch for monitoring

---

## Security Features

- Password hashing using Werkzeug
- Session-based authentication
- File type validation
- Private S3 bucket configuration

---

## Future Improvements

- HTTPS support
- Better user role management
- PostgreSQL database
- Automatic deployment improvements

---

## Author

Adone Varughese  
Internship Project