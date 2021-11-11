FROM maven:3.3.3-jdk-8

MAINTAINER rasesh.desai@gmail.com

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

ADD . /usr/src/app

RUN mvn install

ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","target/spring-boot-service-1-0.0.1-SNAPSHOT.jar"]