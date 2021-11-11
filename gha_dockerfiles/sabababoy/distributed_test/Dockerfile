FROM ubuntu

EXPOSE 22 60000 1099 50000

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR  /home

RUN apt-get update > /dev/null && \
	apt-get upgrade > /dev/null && \
	apt-get -y install openssh-server > /dev/null && \
	apt-get -y install nano > /dev/null && \
	apt -y install default-jdk > /dev/null && \
	apt-get -y install curl > /dev/null

RUN	curl -O https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-5.3.tgz 
RUN	tar -xvf apache-jmeter-5.3.tgz 
RUN	cd apache-jmeter-*/lib 
RUN	curl -O https://repo1.maven.org/maven2/kg/apc/cmdrunner/2.2.1/cmdrunner-2.2.1.jar 
RUN	cd apache-jmeter-*/lib/ext
RUN	curl -O https://repo1.maven.org/maven2/kg/apc/jmeter-plugins-manager/1.6/jmeter-plugins-manager-1.6.jar

RUN mkdir Scripts
	

COPY ./Scripts/ /home/Scripts
