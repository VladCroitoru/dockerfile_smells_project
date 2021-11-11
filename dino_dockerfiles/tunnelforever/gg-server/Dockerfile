FROM anapsix/alpine-java
MAINTAINER outloudvi <outloudvi@outlook.com>

ENV HTTPPORT '8080'

RUN apk add --update openssl
RUN wget https://gogohome.herokuapp.com/getLatestGoGoServer -O /home/gogolatest.jar
EXPOSE 8080 8443
ENTRYPOINT exec java -Xmx300m -jar /home/gogolatest.jar 8080
