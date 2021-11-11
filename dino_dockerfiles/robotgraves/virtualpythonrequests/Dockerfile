FROM robotgraves/virtualpython:latest

RUN apt-get update
RUN apt-get install -y python-pip \
    jq \
    git 

RUN /opt/v/bin/pip install --upgrade requests  \
                           --upgrade bumpversion