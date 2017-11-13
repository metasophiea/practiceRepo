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
                sh 'g++ brokenCPP.cpp'
            }
        }
        stage('Success Build') {
            steps {
                echo 'Building..'
                sh './workingCode.sh'
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
