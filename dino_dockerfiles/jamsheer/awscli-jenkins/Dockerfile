FROM jenkins/jenkins:lts

MAINTAINER Jamsheer Kandoth <jamsheer.kandoth@gmail.com>

USER root
RUN \ 
	wget -O- -q http://s3tools.org/repo/deb-all/stable/s3tools.key | apt-key add - && \
	wget -O /etc/apt/sources.list.d/s3tools.list http://s3tools.org/repo/deb-all/stable/s3tools.list && \
	apt-get -y update && \
	apt-get -y install python-pip python-yaml s3cmd duplicity && \
	pip install awscli boto 
RUN mkdir -p ~/.aws
RUN touch ~/.aws/config
RUN touch ~/.aws/credentials

USER jenkins
