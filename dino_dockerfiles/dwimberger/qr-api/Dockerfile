FROM openjdk:8u111-jre-alpine

MAINTAINER Dieter Wimberger "dieter@wimpi.net"

EXPOSE 4567

RUN apk add --no-cache openssl
RUN mkdir /qr
WORKDIR /qr
RUN wget https://github.com/dwimberger/spark-qr/releases/download/0.0.3/spark-qr-0.0.3.jar
CMD ["java","-jar","spark-qr-0.0.3.jar"]


