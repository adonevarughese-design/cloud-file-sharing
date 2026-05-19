# CloudShare – Secure Cloud File Sharing System

## Project Overview

CloudShare is a secure cloud-based file sharing application developed using Flask and deployed on AWS EC2. The project allows users to register, log in securely, upload files, download files, and manage shared content through a modern web interface.

The application is deployed using Docker, Gunicorn, and Nginx for production-level hosting. AWS services such as EC2, S3, and CloudWatch are integrated for cloud deployment, storage backup, and monitoring.

---

## Features

- User Registration and Login
- Password Hashing and Secure Authentication
- File Upload and Download
- Dark/Light Theme Toggle
- AWS EC2 Deployment
- Docker Containerization
- Nginx Reverse Proxy
- Gunicorn Production Server
- GitHub Version Control
- GitHub Actions CI/CD
- AWS S3 Backup Integration
- CloudWatch Monitoring and Alerts

---

## Technologies Used

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python Flask
- Flask-SQLAlchemy

### DevOps & Cloud
- AWS EC2
- AWS S3
- AWS CloudWatch
- Docker
- Gunicorn
- Nginx
- GitHub Actions

---

## Project Architecture

User Browser
↓
Nginx Reverse Proxy
↓
Docker Container
↓
Gunicorn Server
↓
Flask Application
↓
SQLite Database

---

## Deployment Steps

1. Created AWS EC2 Ubuntu Instance
2. Configured Security Groups
3. Installed Python, Nginx, Docker
4. Cloned GitHub Repository
5. Configured Gunicorn Service
6. Configured Nginx Reverse Proxy
7. Built Docker Container
8. Configured GitHub Actions CI/CD
9. Integrated AWS S3 Backup
10. Configured CloudWatch Monitoring

---

## Security Features

- Password Hashing
- Session-Based Authentication
- Secure File Handling
- Cloud Backup
- Reverse Proxy Protection

---

## Future Enhancements

- HTTPS/SSL Integration
- Multi-user Role Management
- PostgreSQL/RDS Integration
- Automatic Deployment Pipeline
- File Encryption

---

## Author

Adone Varughese
BCA Final Year Project