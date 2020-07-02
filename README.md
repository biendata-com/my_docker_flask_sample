# my_docker_flask_sample for KDD 2020

This is a sample python-based docker submission for KDD 2020 Graph Adversarial Attack & Defense phase 2. We provide a simple API implementation using flask. This repo is already a valid submission by directly serve some of our baseline results. Participants can take the following steps to fit their model in:

1. Download this repo.
2. Add your python dependencies in requirements.txt.
3. Replace model() function with your own model processing code in 'app/views.py'.
4. Add your own files under 'app' directory(if needed).
5. Modify Dockerfile to produce your own environment(if needed).
6. Build your image: sudo docker build -t my_project_name:my_version
7. Test your docker image by running: sudo docker run -p 5000:5000 my_project_name:my_version
8. Compress your image by running: sudo docker save my_project_name:my_version | gzip > my_project_name.tar.gz
9. Upload the tar file on our website https://biendata.xyz/competition/kddcup_2020/final-submission/


Here are some tutorials about how to containerise your machine learning model with docker and flask:

https://medium.com/analytics-vidhya/deploy-your-machine-learning-model-on-docker-ee2b931e133c

https://dev.to/aminu_israel/build-and-deploy-your-machine-learning-application-with-docker-5322

    
    
Good luck!
