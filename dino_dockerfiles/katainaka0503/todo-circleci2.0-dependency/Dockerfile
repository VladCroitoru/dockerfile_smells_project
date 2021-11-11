FROM ubuntu:16.04

# update
RUN set -x && \
  apt-get update
  
# jq
RUN apt-get install -y jq

# aws-cli
RUN apt-get install -y python && \
  apt-get install -y python-pip && \
  pip install --upgrade awscli

# java8
RUN set -x && \
  apt-get install -y software-properties-common && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections && \
  echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 seen true" | debconf-set-selections && \
  apt-get install -y oracle-java8-installer

# sbt
ENV SBT_VERSION=0.13.15
RUN set -x && \
  apt-get install -y curl && \
  curl -L -o sbt-$SBT_VERSION.deb https://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \
  dpkg -i sbt-$SBT_VERSION.deb && \
  rm sbt-$SBT_VERSION.deb && \
  apt-get install -y sbt && \
  sbt sbtVersion

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
