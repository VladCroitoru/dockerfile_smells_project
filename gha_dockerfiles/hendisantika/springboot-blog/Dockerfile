FROM openjdk:8u151-jdk-alpine3.7

MAINTAINER Hendi Santika <hendisantika@yahoo.co.id>

EXPOSE 8080

ENV APP_HOME /usr/src/app

COPY target/springboot-blog-0.0.1-SNAPSHOT.jar $APP_HOME/app.jar

WORKDIR $APP_HOME

ENTRYPOINT exec java -jar app.jar