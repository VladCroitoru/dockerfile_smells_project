FROM openjdk:11.0.10-jre-buster

RUN mkdir /server
WORKDIR /server

COPY ./build/libs/realworld-spring-boot-java-2.0.0.jar .

EXPOSE 8080

CMD ["java","-jar","realworld-spring-boot-java-2.0.0.jar"]

