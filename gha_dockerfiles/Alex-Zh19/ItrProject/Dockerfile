FROM openjdk:16-alpine3.13

WORKDIR /app

COPY build/libs/*SNAPSHOT.jar app/ItrProject.jar

ENTRYPOINT ["java","-jar","app/ItrProject.jar"]
