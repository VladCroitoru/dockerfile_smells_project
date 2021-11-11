FROM maven:3-jdk-7

MAINTAINER Konstantinos Servis <knservis@gmail.com>

COPY . /usr/src/kinesis-s3-persister

ENV KSP_VERSION 1.0

RUN cd /usr/src/kinesis-s3-persister && mvn package
RUN mkdir /opt/kinesis-s3-persister/ && cp /usr/src/kinesis-s3-persister/target/kinesis-s3-persister-1.0-SNAPSHOT-jar-with-dependencies.jar /opt/kinesis-s3-persister/kinesis-s3-persister.jar
RUN cd /usr/src/kinesis-s3-persister && mvn clean
WORKDIR /opt/kinesis-s3-persister/
CMD java -jar kinesis-s3-persister.jar
