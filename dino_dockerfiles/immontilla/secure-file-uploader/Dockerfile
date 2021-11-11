FROM alpine/git as clone
LABEL maintainer="Iván Mauricio Montilla Figueroa"
WORKDIR /app
RUN git clone --progress https://github.com/immontilla/file-uploading-web-app.git

FROM maven:alpine as build
WORKDIR /app
COPY --from=clone /app/file-uploading-web-app /app
RUN mvn -DskipTests=true clean install && cp target/secure-upload-1.0.0.jar app.jar

FROM openjdk:8-jdk-alpine
WORKDIR /app
COPY --from=build /app/app.jar /app
EXPOSE 8090
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","app.jar"]
