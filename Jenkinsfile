node {
   env.WORKSPACE = pwd()

   env.PROJECT_NAME="adamwalach/python-camera-robo-arm-control"
   env.PROJECT_URL="github.com/${env.PROJECT_NAME}"

   env.IMAGE_NAME="awalach/python-camera-robo-arm-control"

   stage 'Check environment'
     echo """
       WORKSPACE: ${env.WORKSPACE}

       PROJECT_NAME: ${env.PROJECT_NAME}
       PROJECT_PATH: ${env.PROJECT_PATH}
     """

   stage 'Cleanup'
     deleteDir()

   stage 'Checkout'
     checkout scm

   stage 'Docker build'
     sh '''
        docker pull awalach/raspbian_lite:jessie_python
        docker build -t $IMAGE_NAME:$BRANCH_NAME ./
     '''

   stage 'Docker push'
     sh '''
       docker push $IMAGE_NAME:$BRANCH_NAME
     '''

   stage 'Deploy'
     ansiblePlaybook([playbook: 'playbook.yml'])

}
