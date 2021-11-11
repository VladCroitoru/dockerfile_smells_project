FROM ubuntu

MAINTAINER Anastas Dancha "carlos.lopezperez@gmail.com"

RUN locale-gen es_ES.UTF-8

ENV LANG es_ES.UTF-8
ENV LANGUAGE es_ES:es
ENV LC_ALL es_ES.UTF-8
ENV NLS_LANG SPANISH_SPAIN.WE8ISO8859P1

## JAVA INSTALLATION
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" > /etc/apt/sources.list.d/webupd8team-java-xenial.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes --no-install-recommends oracle-java8-installer && apt-get clean all
RUN apt install oracle-java8-set-default
## JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle