FROM openjdk:8-jdk-alpine
RUN apk add ttf-dejavu
EXPOSE 8080
COPY target/*.jar app.jar
ENTRYPOINT ["java","-Dspring.profiles.active=rancher","-jar","/app.jar"]