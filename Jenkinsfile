pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh './importantCode.sh'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing 1..'
            },
            steps {
                echo 'Testing 2..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
