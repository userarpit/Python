/*Jenkinsfile (Declarative Pipeline)
 Requires the Docker Pipeline plugin */
pipeline {
    agent any
    triggers {
     cron 'H * * * *'
    }
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
                echo "build number is ${currentBuild.number}"
                echo currentBuild.displayName
                echo currentBuild.fullDisplayName
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                sh 'printenv'
            }
        }
     stage('cat README') {
            when {
                branch "main"
            }
            steps {
               sh '''
                  cat README.md
               '''
               echo "Branch name is ${env.BRANCH_NAME}"
            }
        }
    }
}
