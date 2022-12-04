pipeline {
    agent any
    stages {
      stage('Non-Parallel Stage') {
        agent {
          label 'Master'
        }
        steps {
          echo "This stage will be executed first"
        }
      }
      
      stage('Run Tests') {
        parallel {
          stage('Test on Windows') {
            agent {
              label 'Windows_Node'
            }
            steps {
              echo "Task1 on Agent"
            }
          }
          
          stage('Test on Master') {
            agent {
              label 'Master'
            }
            steps {
              echo "Task1 on Master"
            }
          }
        }
      }

    }
    
    post {
      always {
        echo 'This will always run'
      }
      success {
        echo 'This will run only if successful'
      }
      failure {
        echo 'This will run only if failure'
      }
      unstable {
        echo 'This will run only if the run is marked as unstable'
      }
      changed {
        echo 'This will run only if the state of the Pipeline has changed'
      }
    }    
}
