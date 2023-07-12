/*Jenkinsfile (Declarative Pipeline)
 Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                sh 'python --version'
            }
        }
     stage('Table of 8') {
            steps {
                sh 'python table_of_8.py'
            }
        }
     stage('Factorial') {
            steps {
                sh 'python test1/factorial.py'
                echo 'build number is ${currentBuild.number}'
            }
        }
    }
}
