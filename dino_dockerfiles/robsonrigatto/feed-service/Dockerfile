FROM maven:3.5.2-jdk-8-alpine

WORKDIR /code

ADD pom.xml /code/pom.xml
ADD src /code/src
RUN ["mvn", "clean", "install", "-Dmaven.test.skip=true"]

ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-Dspring.profiles.active=container","-jar","target/feed-service.jar"]