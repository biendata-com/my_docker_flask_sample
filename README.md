# my_docker_flask_sample for KDD 2020

This is a sample submission for KDD 2020 Graph Adversarial Attack & Defense phase 2. We provide a simple API implementation using flask. 

This project, despite its lacking of actual model processing, is already a valid submission by directly serve some of our baseline results. Participants can simply make several modifications to fit their model in, such as:

* modify Dockerfile to produce your own environment.
* add your python dependencies in requirements.txt.
* add your own files under 'app' directory.
* add your own model processing code in 'app/views.py'.
* replace './submit.zip' with your your attack file.
* etc..

Here are some tutorials about how to containerise your machine learning model with docker and flask:

https://medium.com/analytics-vidhya/deploy-your-machine-learning-model-on-docker-ee2b931e133c

https://dev.to/aminu_israel/build-and-deploy-your-machine-learning-application-with-docker-5322

Once you are done, you can build your image:

    sudo docker build -t my_project_name:my_version

Test it on your local machine:

    sudo docker run -p 5000:5000 my_project_name:my_version
    
And finally compress it to upload:

    sudo docker save my_project_name:my_version | gzip > my_project_name.tar.gz
    
    
Good luck!
