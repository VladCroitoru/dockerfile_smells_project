FROM openjdk:8u131-jdk-alpine
WORKDIR /app
VOLUME /app
EXPOSE 8080
ADD /target/travel-0.1.jar travel-0.1.jar
ENTRYPOINT [“java”,“-.jar”,”travel-0.1.jar”]
ONBUILD COPY app.jar /app/app.jar
