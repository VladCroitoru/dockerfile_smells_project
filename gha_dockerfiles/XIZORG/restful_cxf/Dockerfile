FROM adoptopenjdk/openjdk11:latest
VOLUME /tmp
ADD target/spring-rest-sandbox-1.0-SNAPSHOT.jar ./
EXPOSE 8089
ENTRYPOINT ["java","-jar","/spring-rest-sandbox-1.0-SNAPSHOT.jar"]
