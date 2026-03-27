# DevOps Project - Flask Application Deployment

This project demonstrates a complete DevOps workflow starting from source code in GitHub, building CI/CD pipelines using Jenkins and GitHub Actions, containerizing the application using Docker, and deploying it to Kubernetes using Minikube.

---

# Project Structure

devops_final_project/
│

├── app/

│ ├── app.py

│ └── requirements.txt

│

├── k8s/

│ ├── deployment.yaml

│ ├── service.yaml

│ ├── postgres-deployment.yaml

│ └── postgres-service.yaml

│

├── .github/workflows/

│ └── ci.yml

│

├── Dockerfile

├── Jenkinsfile

└── README.md


---

# Project Architecture

GitHub → Jenkins → Docker → Docker Hub → Kubernetes → Flask App + PostgreSQL


---

# Tools Used

| Stage | Tool | Purpose |
|------|------|--------|
| Version Control | GitHub | Store source code |
| CI/CD | Jenkins | Automate pipeline |
| CI/CD Alternative | GitHub Actions | Trigger pipeline on push |
| Containerization | Docker | Build container image |
| Registry | Docker Hub | Store image |
| Orchestration | Kubernetes | Deploy application |
| Local Cluster | Minikube | Run Kubernetes locally |
| Backend | Flask | Web application |
| Database | PostgreSQL | Data storage |

---

# End-to-End Workflow

### 1. Code Update
- Developer pushes code to GitHub repository

### 2. CI/CD Pipeline Trigger
- Jenkins pipeline is triggered automatically
- GitHub Actions workflow also runs on push

### 3. Build Process
- Dependencies installed
- Application validated
- Docker image built

### 4. Docker Image Push
- Image pushed to Docker Hub: docker push paisanjana/devops_flask_app:latest


### 5. Kubernetes Deployment
- Deployment and service applied: kubectl apply -f k8s/

---

# Challenges & Solutions

### Python Package Installation Error
**Issue:**

externally-managed-environment

**Solution:**
- Used virtual environment (venv)

---

###  CrashLoopBackOff in Kubernetes
**Issue:**
- App started before DB ready

**Solution:**
- Added error handling in Flask app

---

# Scaling the Application

kubectl scale deployment flask-app --replicas=3

---

# Outcomes

- Application successfully deployed on Kubernetes
- Multiple pods running
- Database connected
- Application accessible via browser
