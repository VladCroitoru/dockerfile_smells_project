FROM ubuntu:14.04

MAINTAINER Rene Pietzsch <rene.pietzsch@eccenca.com>

# Let the conatiner know that there is no tty
ENV DEBIAN_FRONTEND noninteractive
ENV LNG de
ENV XMX 8G

# update ubuntu trusty
RUN \
	sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
	apt-get update && \
	apt-get -y upgrade && \
    apt-get install -qy ca-certificates build-essential pkg-config && \
    apt-get install -qy software-properties-common && \
    apt-get install -qy dpkg-dev build-essential git supervisor && \
    apt-get install -qy procps curl wget zsh vim unzip htop nmap && \
    apt-get install -qy nullmailer maven graphviz

# Install Java 8.
RUN \
  echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer

RUN mkdir /FOX
ADD FOX /FOX
WORKDIR /FOX
RUN mvn package
WORKDIR /FOX/release
RUN cp fox.properties-dist fox.properties
ADD learn-and-run-fox.sh /FOX/release/learn-and-run-fox.sh
RUN chmod +x /FOX/release/learn-and-run-fox.sh

CMD /FOX/release/learn-and-run-fox.sh

EXPOSE 4444
