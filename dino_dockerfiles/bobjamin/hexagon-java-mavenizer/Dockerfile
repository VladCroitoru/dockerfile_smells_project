FROM ubuntu:14.04

RUN apt-get -y update

# Install java 8.
RUN apt-get -y install software-properties-common
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
RUN apt-add-repository -y ppa:webupd8team/java
RUN apt-get -y update
RUN apt-get -y install oracle-java8-installer

# Install maven.
RUN  apt-get -y install maven

ADD run.sh /run.sh

CMD ["/bin/sh", "/run.sh"]
