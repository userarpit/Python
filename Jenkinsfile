/*Jenkinsfile (Declarative Pipeline)
 Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                sh 'python3 --version'
            }
        }
     stage('Factorial') {
            steps {
                sh 'python3 test1/factorial.py'
                echo "build number is ${currentBuild.number}"
                echo currentBuild.displayName
                echo currentBuild.fullDisplayName
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                sh 'printenv'
            }
        }
     stage('branch name') {
      steps {
       echo "Branch name is ${env.BRANCH_NAME}"
      }
     }
     stage('cat README') {
            when {
                not (branch "main")
            }
            steps {
               sh '''
                  cat README.md
               '''
               echo "Branch name is ${env.BRANCH_NAME}"
               echo "change id ${env.CHANGE_ID}"
            }
        }
    }
}
