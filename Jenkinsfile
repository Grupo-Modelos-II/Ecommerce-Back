pipeline {
    agent none

    stages {
        stage('SCM') {
            agent any
            steps {
                git 'https://github.com/Grupo-Modelos-II/Ecommerce-Back.git'
                stash name: 'source', includes: '**'
            }
        }
        stage('Deploy') {
            agent {
                label 'Glud'
            }
            environment {
                SECRET = credentials('be58a706-061a-4630-84f6-a3b38d0551a9')
                FIREBASE = credentials('7defdf00-fa64-4468-9dc4-6a8c63a6ec8b')
            }
            steps {
                unstash 'source'
                sh 'docker build -t ecommerce_server:latest .'
                sh 'docker-compose -f docker-stack.yml config'
                sh 'cp ${FIREBASE} src/private/'
                sh 'docker stack deploy -c docker-stack.yml ecommerce'
            }
        }
    }
}
