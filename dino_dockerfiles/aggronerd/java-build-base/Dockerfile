FROM maven:3-jdk-8

RUN apt-get update && apt-get install -y apt-transport-https ca-certificates software-properties-common
ADD docker.gpg /tmp/docker.gpg 
RUN apt-key add /tmp/docker.gpg 
RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
   $(lsb_release -cs) \
   stable"
RUN apt-get update && apt-get install -y python-pip python-dev docker-ce
RUN pip install awscli
