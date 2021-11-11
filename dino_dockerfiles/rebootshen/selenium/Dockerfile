FROM ubuntu

ENV VERSION 2.53.0

RUN apt-get update -qqy \
&& apt-get -qqy --no-install-recommends install \
software-properties-common \
&& rm -rf /var/lib/apt/lists/*
RUN add-apt-repository -y ppa:webupd8team/java

RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections

RUN apt-get update -qqy \
&& apt-get -qqy --no-install-recommends install \
oracle-java7-installer \
&& rm -rf /var/lib/apt/lists/*

RUN wget http://selenium-release.storage.googleapis.com/${VERSION%.*}/selenium-server-standalone-${VERSION}.jar
