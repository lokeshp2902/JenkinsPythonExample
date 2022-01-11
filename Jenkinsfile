pipeline {
    agent any
    
    environment {
       TEMP_INTEG_BRANCH = 'temp_integration'                           
    }
    
    stages {
        stage('Jenkins Interface') {
            steps {
                dir('/home/adminspin/office/wsi/JenkinsPythonExample/')
                {
                    script {
                        if(env.ghprbPullDescription.contains("has merge conflicts"))
                        {
                            error('PR has merge conflicts')
                        }
                        sh "git checkout -b ${env.TEMP_INTEG_BRANCH} origin/${ghprbTargetBranch}"
                        sh "git pull origin ${ghprbSourceBranch}"
                    }
                }
            }
        }
        stage('Test') {
            steps {
                dir('/home/adminspin/office/wsi/JenkinsPythonExample/unitTests/')
                {
                    sh "pytest"
                }
            }
        }
    }
    post {
        always {
            dir("/home/adminspin/office/wsi/JenkinsPythonExample/"){
                sh "git checkout main"
                sh "git branch -D ${env.TEMP_INTEG_BRANCH}"
            }
        }
    }
}
