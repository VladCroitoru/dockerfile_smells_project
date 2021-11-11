 
FROM openjdk:11-jdk-slim

ADD target/covid*.jar app.jar

ENTRYPOINT ["java", "-jar", "app.jar" ]
