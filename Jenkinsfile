pipeline {

    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/aditirewadkar3/AWDLISEpart2.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Train ML Model') {
            steps {
                bat 'python train_model.py'
            }
        }

        stage('Run FastAPI') {
            steps {
                bat 'start run_fastapi.bat'
            }
        }

        stage('Display URL') {
            steps {
                bat 'echo http://127.0.0.1:8091'
            }
        }
    }
}