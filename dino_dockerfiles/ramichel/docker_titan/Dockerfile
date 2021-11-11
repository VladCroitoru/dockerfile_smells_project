FROM ubuntu:14.04

MAINTAINER Raymond Michel <raym.michel@gmail.com>

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update
# RUN apt-get install -y software-properties-common

# install java8
# RUN add-apt-repository -y ppa:webupd8team/java
# RUN apt-get update
# RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections

# install all our dependancies
RUN apt-get install -y \
	unzip \
	curl \
	git \
	python2.7 \
	python-pip

WORKDIR /opt/titan-0.5.4-hadoop2

# Grab the Titan 0.5.4 package and unzip it
RUN curl -o /opt/titan.zip http://s3.thinkaurelius.com/downloads/titan/titan-0.5.4-hadoop2.zip
RUN unzip /opt/titan.zip -d /opt/ && \
    rm /opt/titan.zip

# Add the custom Rexster files for the Docker implementation
ADD rexster-titan.xml.template /opt/titan-0.5.4-hadoop2/
ADD run.sh /opt/titan-0.5.4-hadoop2/
RUN chmod +x run.sh

# expose our necessary ports
EXPOSE 8182
EXPOSE 8183
EXPOSE 8184
EXPOSE 9160
CMD ["/bin/sh", "-e", "/opt/titan-0.5.4-hadoop2/run.sh"]
