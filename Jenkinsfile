pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                cleanWs()
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Installs pytest locally on the Windows host machine
                bat "pip install pytest"
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Executes pytest with the verbose (-v) flag
                bat "pytest -v"
            }
        }
    }
}
