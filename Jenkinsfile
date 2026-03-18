pipeline {
    agent any

    environment {
        SONAR_TOKEN = credentials('sonar-token')
        SONAR_URL   = "http://172.25.124.56:9000"
    }

    stages {

        stage('Unit Tests') {
            steps {
                sh '''
                    cd app
                    pip3 install -r requirements.txt --break-system-packages
                    python3 -m pip install pytest pytest-cov --break-system-packages
                    python3 -m pytest -v
                '''
            }
        }

        stage('SonarQube Scan') {
            steps {
                sh '''
                    sonar-scanner \
                      -Dsonar.projectKey=Prodstack \
                      -Dsonar.sources=app \
                      -Dsonar.host.url=${SONAR_URL} \
                      -Dsonar.token=${SONAR_TOKEN}
                '''
            }
        }

    }

    post {
        success { echo "Pipeline passed" }
        failure { echo "Pipeline failed" }
    }
}
