FROM openjdk:8-jre-slim
COPY ./build/libs/Backend-Infowargame-v3-0.0.1-SNAPSHOT.jar app.jar
RUN mkdir -p /home/ubuntu/images
ENTRYPOINT ["java", "-jar", "-Xmx200m", "/app.jar"]
EXPOSE 7001