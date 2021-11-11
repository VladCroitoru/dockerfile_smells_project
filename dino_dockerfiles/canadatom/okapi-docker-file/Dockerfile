############################################################
# Dockerfile to build Okapi Installed Containers
# Based on Ubuntu:latest
############################################################

# Set the base image to Ubuntu
FROM ubuntu

# File Author / Maintainer
MAINTAINER Maintaner Tom Wu <tomoodesign@gmail.com>

# Pre-requisite for compiling Okapi
RUN dpkg --add-architecture i386
RUN apt-get update
RUN apt-get install -y \
	gcc \
	gcc-multilib \
	libc6-i386 \
	make \
	bison \
	flex \
	openjdk-6-jdk:i386 \
	git \
	vim

# jdk 6 and gcc 4.8
RUN cp /usr/lib/jvm/java-1.6.0-openjdk-i386/include/jni.h /usr/lib/gcc/x86_64-linux-gnu/4.8/include
RUN cp /usr/lib/jvm/java-1.6.0-openjdk-i386/include/jni_md.h /usr/lib/gcc/x86_64-linux-gnu/4.8/include

RUN mkdir -p /home/okapi
RUN git clone https://github.com/canadatom/okapi.git /home/okapi
RUN git config --global user.email "tomoodesign@gmail.com"
RUN git config --global user.name "Tom Wu"

# initialize okapi
RUN /home/okapi/scripts/init.sh

WORKDIR /home/okapi

