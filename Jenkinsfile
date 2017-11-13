pipeline {
  agent any
  stages {
    stage('Fail Build') {
      steps {
        echo 'Building..'
        sh './brokenCode.sh'
      }
    }
    stage('Fail Compile') {
      steps {
        echo 'Compiling..'
      }
    }
    stage('Success Build') {
      parallel {
        stage('Success Build') {
          steps {
            echo 'Building..'
            sh './workingCode.sh'
          }
        }
        stage('') {
          steps {
            echo 'Look at this'
          }
        }
      }
    }
    stage('Test') {
      steps {
        echo 'Testing..'
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying....'
      }
    }
  }
}