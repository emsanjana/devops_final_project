pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "paisanjana/devops_flask_app:latest"
        DB_HOST = "your_db_host"
        POSTGRES_DB = "your_db_name"
        POSTGRES_USER = "your_db_user"
        POSTGRES_PASSWORD = "your_db_password"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/emsanjana/devops_final_project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r app/requirements.txt'
            }
        }

        stage('Lint & Validate') {
            steps {
                sh 'python -m py_compile app/app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub-credentials', url: '']) {
                    sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
