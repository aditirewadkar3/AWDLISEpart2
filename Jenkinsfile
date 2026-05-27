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

        stage('Train Model') {
            steps {
                bat 'python train_model.py'
            }
        }

        stage('Start FastAPI') {
            steps {
                bat '''
                start "" cmd /c "cd /d C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\IrisDataset1 && python -m uvicorn app:app --host 127.0.0.1 --port 8091"
                '''
            }
        }

        stage('Done') {
            steps {
                bat 'echo FastAPI Started on http://127.0.0.1:8091'
            }
        }
    }
}