FROM openjdk:11-jdk
ADD . /app
WORKDIR /app
RUN cp /app/build/libs/integration-0.0.1-SNAPSHOT.jar /app/integration.jar
CMD ["chmod +x integration.jar"]
ENTRYPOINT ["java","-jar","integration.jar"]