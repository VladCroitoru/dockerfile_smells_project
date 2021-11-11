FROM alpine:3.5

RUN apk add openjdk8-jre-base ca-certificates --update &&\
  rm -rf /var/cache/apk/*

ENV JAR_URL=https://s3-eu-west-1.amazonaws.com/softwaremill-public/elasticmq-server-0.13.2.jar
WORKDIR /elasticmq

ADD $JAR_URL elasticmq-server.jar

ADD custom.conf /elasticmq/custom.conf
CMD ["java", "-Dconfig.file=/elasticmq/custom.conf", "-jar", "/elasticmq/elasticmq-server.jar"]
EXPOSE 80
