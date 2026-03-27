# DevOps Final Project

## Project Overview
This project demonstrates a complete DevOps workflow using a Flask application connected to PostgreSQL, including:

- GitHub for source code management
- CI/CD pipelines using Jenkins and GitHub Actions
- Docker containerization
- Kubernetes deployment

## Project Structure

devops_final_project/

├── app/

│ ├── app.py

│ └── requirements.txt

├── Dockerfile

├── Jenkinsfile

├── .github/workflows/ci-cd.yml

├── k8s/

│ ├── deployment.yaml

│ └── service.yaml

└── README.md


## Application Features
- '/' : Returns all users from the database
- '/add/<name>' : Adds a new user to the database

## Environment Variables Required
- 'DB_HOST'
- 'POSTGRES_DB'
- 'POSTGRES_USER'
- 'POSTGRES_PASSWORD'
