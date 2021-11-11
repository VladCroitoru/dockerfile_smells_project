FROM adoptopenjdk/openjdk11:latest
COPY target/*-0.0.1-SNAPSHOT.jar /health-service.jar
CMD java -jar /health-service.jar
ENTRYPOINT [ "java", "-jar", "/health-service.jar" ]