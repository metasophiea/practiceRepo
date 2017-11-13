pipeline {
    agent any

    stages {
        stage('Fail Build') {
            steps {
                echo 'Building..'
                sh './brokenCode.sh'
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
