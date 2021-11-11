#start from ubuntu base image
FROM ubuntu:14.04

#install oracle java 8
RUN apt-get update
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:webupd8team/java -y
RUN apt-get update
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
RUN apt-get install oracle-java8-installer -y
RUN apt-get install oracle-java8-set-default

#get Producer jar and run
COPY jars /home/root/excercise
WORKDIR /home/root/excercise

#run instns
#Pull and run consumer container first
#Pull producer container from Docker hub
#docker pull annesrinivas/producer
#Run container linking it to Consumer container. Alias of cs
#docker run  -it --name producer --link consumer:cs annesrinivas/producer /bin/bash
# Get IP of container by hosts file or docker inspect
#cat /etc/hosts for IP of consumer
# Run executable jar with IP
#java -jar Producer.jar <ip of consumer>