pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'phoebe-products:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout your Flask application code from a Git repository
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/phoebenoubissi/Product-Mini-App']]])

                script {
                    sshagent(credentials: ['ba987622-3627-420e-8c09-018d8b015c51']) {
                        // Clone your Git repository or perform SSH operations here
                        sh 'git clone https://github.com/phoebenoubissi/Product-Mini-App'
                    }
                }
            }
        }

        stage('Build and Test') {
            steps {
                script {
                    // Build your Flask application (you can adjust this based on your actual build command)
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Dockerize') {
            steps {
                script {
                    // Build a Docker image for your Flask application
                    sh 'sudo visudo'
                    sh 'phoebenoubissi ALL=(ALL) NOPASSWD: /usr/bin/docker build -t $DOCKER_IMAGE .'
                    //sh 'sudo docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Deploy your Docker container (adjust this based on your deployment strategy)
                    sh 'sudo docker run -d -p 5000:5000 $DOCKER_IMAGE'
                }
            }
        }
    }

    post {
        failure {
            mail to: 'phoebesi20@gmail.com', subject: 'Flask App Build and Deployment Failed', body: "The Jenkins job for your Flask app failed. Please check the logs."
        }
    }
}