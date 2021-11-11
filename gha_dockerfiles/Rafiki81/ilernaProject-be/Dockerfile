FROM adoptopenjdk:11-jre-hotspot
EXPOSE 8080
WORKDIR /app
COPY target/ilernaProject-be-0.0.1-SNAPSHOT.jar .
ENTRYPOINT ["java", "-jar", "ilernaProject-be-0.0.1-SNAPSHOT.jar"]