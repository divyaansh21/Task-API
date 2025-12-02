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
                    sh "docker stop ${APP_NAME} || true"
                    sh "docker rm ${APP_NAME} || true"
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${APP_NAME}:latest ."
            }
        }

        // ---TEST STAGE ---
        stage('Unit Test') {
            steps {
                echo "Running Unit Tests inside the container..."
                // This runs the python test script inside the image we just built
                sh "docker run --rm ${APP_NAME}:latest python -m unittest test_app.py"
            }
        }
        // ----------------------
        
        stage('Deploy Application') {
            steps {
                sh "docker run -d --name ${APP_NAME} -p ${HOST_PORT}:${CONTAINER_PORT} ${APP_NAME}:latest"
            }
        }
        
        stage('Verify Deployment') {
            steps {
                echo "Waiting for application to initialize..."
                sleep 10
                sh "curl -f http://localhost:${HOST_PORT} || (docker logs ${APP_NAME} && exit 1)"
            }
        }
    }
}
