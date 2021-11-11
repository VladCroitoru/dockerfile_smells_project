FROM jenkins/jenkins:2.60.3

USER root
RUN apt-get update && apt-get install -y \
    python-pip \
    virtualenv \
    libblas-dev \
    liblapack-dev \
    libfreetype6-dev 
    

USER jenkins
