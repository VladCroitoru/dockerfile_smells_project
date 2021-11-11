FROM ubuntu:16.04

MAINTAINER Martin Simoneau "martin1.simoneau@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

# Set Timezone to Montreal
RUN echo "America/Montreal" > /etc/timezone; dpkg-reconfigure -f noninteractive tzdata

## Set LOCALE to UTF8
RUN apt-get install -y locales
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen en_US.UTF-8 && \
    dpkg-reconfigure locales && \
    /usr/sbin/update-locale LANG=en_US.UTF-8

ENV LC_ALL en_US.UTF-8

# Install dev and utilities.
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y software-properties-common && \
    apt-get install -y openssh-server && \
    apt-get install -y git build-essential && \
    apt-get install -y openssl libssl-dev && \
    apt-get install -y wget curl tcpdump zip unzip libfontconfig1-dev python gradle && \
    apt-get autoclean

## Install Java 8
RUN add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections && \
    echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 seen true" | debconf-set-selections && \
    apt-get install -y oracle-java8-installer
RUN apt-get install -y oracle-java8-set-default

# Define JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

## Groovy 2.7
RUN cd /tmp && \
    wget http://dl.bintray.com/groovy/maven/apache-groovy-binary-2.4.7.zip && \
    unzip apache-groovy-binary-2.4.7.zip && \
    mv groovy-2.4.7 /groovy && \
    rm apache-groovy-binary-2.4.7.zip
ENV GROOVY_HOME /groovy
ENV PATH $GROOVY_HOME/bin/:$JAVA_HOME/bin:$PATH

# Add a user.
ARG user=admin
RUN adduser --disabled-password --gecos '' ${user} && \
    adduser ${user} sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
    usermod -s /bin/bash ${user}

ENV HOME /home/${user}
WORKDIR ${HOME}

VOLUME ["${HOME}/sources"]

USER ${user}
