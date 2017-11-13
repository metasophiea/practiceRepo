pipeline {
  agent any
  stages {
    stage('Stage 1 Builds') {
      parallel {
        stage('Fail Build Script') {
          steps {
            echo 'Running the unsuccessful build script'
            sh './brokenCode.sh'
          }
        }
        stage('Fail Compile') {
          steps {
            echo 'Attempting to compile "brokenCPP.cpp"'
            sh '''g++ brokenCPP.cpp || true
# Force progression'''
          }
        }
        stage('Success Build Script') {
          steps {
            echo 'Running the successful build script'
            sh './workingCode.sh'
          }
        }
        stage('Success Compile') {
          steps {
            echo 'Attempting to compile "workingCPP.cpp"'
            sh 'g++ workingCPP.cpp'
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