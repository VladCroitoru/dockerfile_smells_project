# CaMicroscope DATA container
# DOCKER-VERSION 0.3.4
# Mongo, Bindass

# VERSION               0.3.1

#FROM     alpine:latest
FROM ubuntu:16.04
MAINTAINER Ganesh Iyer "lastlegion@gmail.com"

# build with
#  sudo docker build --rm=true -t="repo/imgname" .

### update
RUN apt-get -q update
RUN apt-get -q -y upgrade
RUN apt-get -q -y dist-upgrade
RUN apt-get install -q -y libcurl3 

# Java
RUN mkdir /root/src

WORKDIR /root/src
RUN  apt-get install -y default-jdk
#RUN sudo apt-get install -y openjdk-8-jre
# Add java to path

ENV PATH /root/src/jre1.6.0_45/bin:$PATH
 

# Bindaas
RUN mkdir -p /root/bindaas

ADD http://imaging.cci.emory.edu/wiki/download/attachments/4915228/bindaas-dist-2.0.2-201603312230-min.tar.gz?version=1&modificationDate=1459806174096&api=v2 /root/bindaas/bindaas.tar.gz
WORKDIR /root/bindaas
RUN tar -xvf bindaas.tar.gz && rm bindaas.tar.gz
COPY projects /root/bindaas/bin/projects


COPY bindaas.config.json /root/bindaas/bin/
COPY trusted-applications.config.json /root/bindaas/bin/trusted-applications.config.json

EXPOSE 9099
#EXPOSE 8080
WORKDIR /root/bindaas/bin

#WORKDIR /root/scripts
COPY /run.sh /root/bindaas/bin/run.sh


CMD ["sh", "run.sh"]
