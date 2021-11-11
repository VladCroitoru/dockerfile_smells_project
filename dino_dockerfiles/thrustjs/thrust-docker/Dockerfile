FROM debian:latest

ENV THRUST_VERSION 0.5.4

ENV DEBIAN_FRONTEND noninteractive

# auto validate license
RUN apt-get update && \
    apt install -y locales curl software-properties-common gnupg && \
    echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list && \
    echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && apt-get update && apt-get install -y curl dnsutils oracle-java8-installer ca-certificates && \
    locale-gen en_US.UTF-8 en_us && dpkg-reconfigure locales && dpkg-reconfigure locales && locale-gen C.UTF-8 && /usr/sbin/update-locale LANG=C.UTF-8

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8


RUN wget https://github.com/Thrustjs/thrust/releases/download/${THRUST_VERSION}/thrust_${THRUST_VERSION}_all.deb && \ 
    dpkg -i thrust_${THRUST_VERSION}_all.deb