FROM jenkins
MAINTAINER scott@rastermedia.com

USER root

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y python-software-properties software-properties-common
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections
RUN add-apt-repository ppa:webupd8team/java
RUN apt-get update && apt-get -y install git-core oracle-java8-installer jenkins python-pip mysql-client
RUN pip install awscli

USER jenkins
