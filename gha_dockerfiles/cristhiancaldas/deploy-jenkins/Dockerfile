FROM openjdk:11-jre

WORKDIR /

RUN mkdir app && chmod 777 app

COPY target/app-user-0.0.1-SNAPSHOT.jar  /app

WORKDIR /app

EXPOSE 8083

CMD ["java","-jar","app-user-0.0.1-SNAPSHOT.jar"]