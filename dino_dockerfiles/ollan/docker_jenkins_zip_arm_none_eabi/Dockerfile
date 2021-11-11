FROM jenkins/jenkins:latest

MAINTAINER Johan Axfors <johan@axfors.se>

ENV DEBIAN_FRONTEND noninteractive

USER root

RUN mkdir /var/lib/apt/lists/partial

RUN apt-get update && \ 
	apt-get -y install \
    	binutils-arm-none-eabi \
		arm-none-eabi-* \
		gcc \
		make \
		expect \
		zip && \
	apt-get autoremove && \
	apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/apt/archive/*.deb
    
    USER jenkins
