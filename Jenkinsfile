pipeline {
    agent any

    environment {
        SONAR_TOKEN = credentials('sonar-token')
        SONAR_URL   = "http://localhost:9000"
    }

    stages {

        stage('Unit Tests') {
            steps {
                sh '''
                    cd app
                    pip3 install -r requirements.txt --break-system-packages
                    python3 -m pytest -v
                '''
            }
        }

        stage('SonarQube Scan') {
            steps {
                sh '''
                    docker run --rm \
                      --network host \
                      -v $(pwd):/usr/src \
                      sonarsource/sonar-scanner-cli \
                      -Dsonar.projectKey=Prodstack \
                      -Dsonar.sources=app \
                      -Dsonar.host.url=${SONAR_URL} \
                      -Dsonar.token=${SONAR_TOKEN}
                '''
            }
        }

        stage('Terraform Init') {
            steps {
                sh '''
                    cd terraform
                    terraform init
                '''
            }
        }

        stage('Terratest') {
            steps {
                sh '''
                    cd test
                    go test -v -timeout 10m ./...
                '''
            }
        }

    }

    post {
        success {
            echo "Pipeline passed"
        }
        failure {
            echo "Pipeline failed"
        }
    }
}
