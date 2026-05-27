pipeline {

    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/aditirewadkar3/AWDLISEpart2.git'
            }
        }

        stage('Train ML Model') {
            steps {
                bat 'python train_model.py'
            }
        }

       
        stage('Stop Old Container') {
            steps {
                bat 'docker stop fastapi-container || exit 0'
                bat 'docker rm fastapi-container || exit 0'
            }
        }

        
        stage('Display Application URL') {
            steps {
                bat 'echo Application running at http://localhost:8082'
                bat 'echo Swagger UI at http://localhost:8082/docs'
            }
        }

    }
}