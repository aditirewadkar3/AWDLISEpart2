pipeline {

    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/mohinideshmukh765/Heart_Prediction.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t fastapi-ml-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat 'docker stop fastapi-container || exit 0'
                bat 'docker rm fastapi-container || exit 0'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run -d -p 8082:8000 --name fastapi-container fastapi-ml-app'
            }
        }

    }
}