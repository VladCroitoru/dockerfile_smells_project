FROM ubuntu:14.10

MAINTAINER Maksym Bodnarchuk <bodnarchuk@gmail.com>

ENV REFRESHED_AT 2015-02-10

RUN apt-get update

RUN apt-get install -y openjdk-8-jdk

ADD ./src /src
RUN mkdir -p /out
RUN javac -d /out /src/io/healthsamurai/JavaWebServer.java
RUN cp -r /src/META-INF out

WORKDIR /out

RUN jar cmf META-INF/MANIFEST.MF JavaWebServer.jar io

EXPOSE 11133

CMD ["java", "-jar", "JavaWebServer.jar"]