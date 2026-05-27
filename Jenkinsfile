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

        stage('Run FastAPI Server') {
            steps {
                bat '''
                powershell -Command "Start-Process cmd -ArgumentList '/k cd /d C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\IrisDataset1 && python -m uvicorn app:app --host 127.0.0.1 --port 8091 --reload'"
                '''
            }
        }

        stage('Display Application URL') {
            steps {
                bat 'echo Application running at http://127.0.0.1:8091'
                bat 'echo Swagger UI at http://127.0.0.1:8091/docs'
            }
        }

    }
}