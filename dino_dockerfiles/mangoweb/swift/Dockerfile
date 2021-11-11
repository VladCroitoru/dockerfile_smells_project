FROM swiftdocker/swift:latest

MAINTAINER manGoweb.cz (rafaj@mangoweb.cz)
LABEL Description="Ubuntu 16.04 image + Swift + Java & Ruby & Python"


USER root

RUN apt-get -y update
RUN apt-get -y install apt-utils
  
RUN apt-get -y install libcurl4-openssl-dev openssl
RUN apt-get -y install wget curl
RUN apt-get -y install default-jre default-jdk
RUN apt-get -y install ruby-full
RUN apt-get -y install unzip git
RUN apt-get -y install libpq-dev
RUN apt-get -y install libxml2-dev

RUN curl -sL https://check.vapor.sh | bash
#RUN curl -sL https://apt.vapor.sh | bash
RUN apt-get -q install -y software-properties-common python-software-properties apt-transport-https
RUN wget -q https://repo.vapor.codes/apt/keyring.gpg -O- | apt-key add -
RUN echo "deb https://repo.vapor.codes/apt trusty main" | tee /etc/apt/sources.list.d/vapor.list
RUN apt-get -q update

CMD /bin/bash