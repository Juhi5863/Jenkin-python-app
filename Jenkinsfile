pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Juhi5863/Jenkin-python-app.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                pytest test_app.py --disable-warnings
                '''
            }
        }
        stage('Build & Archive') {
            steps {
                sh '''
                mkdir -p build
                cp app.py build/
                cp requirements.txt build/
                cp setup.py build/
                tar -czf build.tar.gz build
                '''
                archiveArtifacts artifacts: 'build.tar.gz', fingerprint: true
            }
        }
    }
}
