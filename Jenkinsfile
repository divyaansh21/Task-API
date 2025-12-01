pipeline {
    agent any
    
    environment {
        APP_NAME = "flask-crud-api"
        HOST_PORT = "9000"
        CONTAINER_PORT = "5000"
    }

    stages {
        stage('Cleanup Old Deployments') {
            steps {
                script {
                    // Stops any existing container so we can deploy the new one
                    sh "docker stop ${APP_NAME} || true"
                    sh "docker rm ${APP_NAME} || true"
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                // Builds the 'installer' package (Docker image)
                sh "docker build -t ${APP_NAME}:latest ."
            }
        }
        
        stage('Deploy Application') {
            steps {
                // Runs the application on port 9000
                sh "docker run -d --name ${APP_NAME} -p ${HOST_PORT}:${CONTAINER_PORT} ${APP_NAME}:latest"
            }
        }
        
        stage('Verify Deployment') {
            steps {
                // Checks if the app is actually alive
                sleep 10
                sh "curl -f http://localhost:${HOST_PORT} || exit 1"
            }
        }
    }
}
