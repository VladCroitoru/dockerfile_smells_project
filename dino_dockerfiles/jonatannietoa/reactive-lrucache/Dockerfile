FROM maven:3.3.3-jdk-8

MAINTAINER jonatannietoa@gmail.com

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

ADD . /usr/src/app

RUN mvn install

ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","target/reactive-lrucache-1.0.0-SNAPSHOT.jar"]