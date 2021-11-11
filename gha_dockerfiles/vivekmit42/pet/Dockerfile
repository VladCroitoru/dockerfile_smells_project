FROM ubuntu
MAINTAINER Vivek <vivekmit42@yahoo.com>
WORKDIR /home
ENV JAVA_VERSION 7
RUN \
  apt-get update && \
  apt-get upgrade -y && \
  apt-get install maven -y && \
  apt-get install openjdk-11-jre -y

RUN update-alternatives --display java
COPY /var/lib/jenkins/jobs/petclinic/spring-petclinic-2.5.0-SNAPSHOT.jar /home/spring-petclinic-2.5.0-SNAPSHOT.jar
CMD java -jar /home/spring-petclinic-2.5.0-SNAPSHOT.jar
