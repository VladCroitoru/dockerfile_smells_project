FROM openjdk:16
ADD web/build/libs/certificates.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]