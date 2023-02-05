import groovy.json.JsonSlurperClassic

def parallel StagesMag

def generateStage(job) {
  return {
    stage ("stage: ${job}") {
      def nodeLabel = job.label
      def jobName = job.test
      node(nodeLabel) {
        echo "This is ${jobName} running on ${nodeLabel}."
        checkout([$class: 'GitSCM',
                  branches: [[name: '*/main']],
                  extensions: [
                    $class: 'CloneOption',
                    shallow: true,
                    depth: 1,
                    timeout: 30],
                  userRemoteConfigs: [[
                    credentialsId: '3549018d-f3bb-4c73-ab8c-5ae89bcf4d72',
                    url: 'https://github.com/reneweb94/hello-World'
                  ]]
                 ])
        bat 'python hello_world'
      }
    }
  }
}

pipeline {
  agent {label 'master'}
  stages {
    stage('Create List of Stages') {
      steps {
        bat 'python fetch_testplan.py --project kepler --testplan=kepler_A0_testplan --loops 10 --filename=testlist.json'
        script {
          echo "Loading Testplan from file"
          def testplan = readJSON file:'testlist.json'
          echo "${testplan}"
          parallelStagesMap = testplan.collectEntries {
            ["${it}" : generateStage(it)]
          }
        }
      }
    }
  
    stage('Run Stages in Parallel') {
      steps {
        script {
          parallel parallelStagesMap
        }
      }
    }
  }
}
