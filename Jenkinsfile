pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.build("naima_flask-app:${env.BUILD_ID}")
                }
            }
        }

        stage('Push to Docker Registry') {
            steps {
                script {
                    // Push Docker image to registry (if needed)
                    // docker.withRegistry('https://registry.example.com', 'docker-credentials-id') {
                    //     docker.image("naima_flask-app:${env.BUILD_ID}").push()
                    // }
                }
            }
        }

        stage('Deploy to Virtual Machine') {
            steps {
                script {
                    // Deploy Docker image on the virtual machine
                    // sshagent(['ssh-credentials-id']) {
                    //     sh 'ssh user@hostname "docker pull naima_flask-app:${env.BUILD_ID} && docker run -d -p 5000:5000 naima_flask-app:${env.BUILD_ID}"'
                    // }
                }
            }
        }
    }

    post {
        always {
            // Cleanup: Remove Docker image locally after deployment
            script {
                docker.image("naima_flask-app:${env.BUILD_ID}").remove()
            }
        }
    }
}
