FROM openjdk:8-jre-alpine
MAINTAINER thimico
EXPOSE 9444
EXPOSE 9191

ENV VERSION=2.7

RUN mkdir /s3ninja
ADD https://oss.sonatype.org/content/groups/public/com/scireum/s3ninja/${VERSION}/s3ninja-${VERSION}-zip.zip /s3ninja/s3ninja.zip
RUN cd /s3ninja && unzip /s3ninja/s3ninja.zip
RUN rm /s3ninja/s3ninja.zip
RUN mkdir -m 777 -p /s3ninja/data/s3

WORKDIR /s3ninja
ENV JAVA_OPTS=""
CMD java ${JAVA_OPTS} -server -Djava.net.preferIPv4Stack=true -Dport=9191 IPL