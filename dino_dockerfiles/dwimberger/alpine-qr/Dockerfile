FROM openjdk:8u111-jre-alpine

MAINTAINER Dieter Wimberger "dieter@wimpi.net"

RUN mkdir /zxing
RUN mkdir /qr

WORKDIR /zxing

RUN wget http://repo1.maven.org/maven2/com/google/zxing/core/3.3.0/core-3.3.0.jar
RUN wget http://repo1.maven.org/maven2/com/google/zxing/javase/3.3.0/javase-3.3.0.jar
RUN wget http://repo1.maven.org/maven2/com/beust/jcommander/1.58/jcommander-1.58.jar

COPY qrdecode /usr/bin/qrdecode
COPY qrencode /usr/bin/qrencode

RUN chmod a+x /usr/bin/qrdecode 
RUN chmod a+x /usr/bin/qrencode 

WORKDIR /qr


