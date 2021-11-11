FROM ubuntu:14.04
MAINTAINER docker@hightml.com


# From Ubuntu Dockerfile
#
# https://github.com/dockerfile/ubuntu

# Install.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y byobu curl git htop man unzip vim wget && \
  rm -rf /var/lib/apt/lists/*

# Add files.
ADD root/.bashrc /root/.bashrc
ADD root/.gitconfig /root/.gitconfig
ADD root/.scripts /root/.scripts

# Set environment variables.
ENV HOME /root




#
# Oracle Java 8 Dockerfile
#
# https://github.com/dockerfile/java
# https://github.com/dockerfile/java/tree/master/oracle-java8
#
# Install Java.
RUN \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer


# Define working directory.
WORKDIR /data

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle




#
# HighTML's Tess4J installation


ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -q -y install software-properties-common

RUN apt-get update




RUN apt-get -q -y install libleptonica-dev
RUN apt-get -q -y install libtesseract3 libtesseract-dev

RUN apt-get -q -y install tesseract-ocr
RUN apt-get -q -y install tesseract-ocr-eng tesseract-ocr-fra tesseract-ocr-nld




RUN ln -s /usr/share/tesseract-ocr/tessdata /data/tessdata


RUN java -version
RUN tesseract --version



CMD ["bash"]

