FROM adoptopenjdk/openjdk11:alpine-jre
COPY  build/libs/xdns-0.0.1-SNAPSHOT.jar  app.jar
EXPOSE 8080
ENTRYPOINT ["java","-jar","/app.jar"]
