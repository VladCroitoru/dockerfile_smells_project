FROM ubuntu:14.04
MAINTAINER kolkos

RUN apt-get update && apt-get install -y python-software-properties software-properties-common
RUN add-apt-repository ppa:webupd8team/java

RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 boolean true" | debconf-set-selections

RUN apt-get update && apt-get install -y oracle-java8-installer maven

ADD . /usr/local/cryptoManager
RUN cd /usr/local/cryptoManager && mvn install
CMD ["java", "-jar", "/usr/local/cryptoManager/target/cryptoManager-0.1.jar"]
