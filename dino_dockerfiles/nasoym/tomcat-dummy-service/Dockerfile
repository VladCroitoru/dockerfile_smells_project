FROM tomcat:8

MAINTAINER Sinan Goo 

RUN apt-get update ; apt-get install -y openjdk-8-jdk 

RUN mkdir -p /spring_service
WORKDIR /spring_service

COPY build.gradle gradlew gradlew.bat /spring_service/
COPY gradle /spring_service/gradle
COPY src /spring_service/src

RUN ./gradlew war

EXPOSE 8080
EXPOSE 8009

RUN cp ./build/libs/spring_service.war /usr/local/tomcat/webapps/hello.war

