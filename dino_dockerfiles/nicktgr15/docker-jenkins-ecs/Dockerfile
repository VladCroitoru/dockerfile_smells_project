FROM jenkins:1.596

USER root
RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

RUN apt-get update
RUN apt-get install python-pip libssl-dev -y
RUN pip install awscli
RUN pip install boto3
RUN pip install virtualenv

COPY deploy.py /usr/bin/deploy
RUN chmod +x /usr/bin/deploy

USER jenkins

COPY gitconfig /var/jenkins_home/.gitconfig
COPY credentials /var/jenkins_home/.aws/credentials
