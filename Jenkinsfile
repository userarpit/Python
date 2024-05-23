/*Jenkinsfile (Declarative Pipeline)
 Requires the Docker Pipeline plugin */
pipeline {
    agent {
     label {
            label 'windows'
            retries 1
        }
    }
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
       echo "change id ${env.CHANGE_ID}"
      }
     }
    }
}
