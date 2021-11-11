FROM openjdk:8-alpine

COPY target/uberjar/grand-central.jar /grand-central/app.jar

EXPOSE 3000

CMD ["java", "-jar", "/grand-central/app.jar"]
