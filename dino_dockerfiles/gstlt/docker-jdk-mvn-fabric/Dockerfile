#
#  Author: Grzegorz Adamowicz
#  Date: 2016/07/01 (Fri, 1st of July 2016)
#
#
# vim: set ts=4 sw=4 tw=0 et

FROM ubuntu:latest
MAINTAINER Grzegorz Adamowicz (gadamowicz@gstlt.info)

LABEL Description="Ubuntu + Oracle Java + Maven + Fabric"

ENV JAVA_HOME=/usr/lib/jvm/java-8-oracle

RUN apt-get update -y
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
RUN apt-get install --no-install-recommends -y software-properties-common
RUN add-apt-repository ppa:webupd8team/java && \
    apt-get update

RUN apt-get install --no-install-recommends -y oracle-java8-installer oracle-java8-set-default && \
    apt-get install --no-install-recommends -y maven && \
    apt-get install -y git python python-pip python-dev

RUN apt-get clean

RUN pip install fabric

CMD /bin/bash


