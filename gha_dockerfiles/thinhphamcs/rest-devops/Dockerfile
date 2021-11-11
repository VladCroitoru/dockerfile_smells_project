FROM openjdk:8-jdk-alpine
# copy the generated JAR into the container 
COPY /target/UserApi-0.0.1-SNAPSHOT.jar UserApi-0.0.1-SNAPSHOT.jar
# From the container I want to expose the port 5000 so I can access it so I can connect my AWS BeanStalk
EXPOSE 5000
# Execute the jar through this commands
ENTRYPOINT ["java", "-jar", "/UserApi-0.0.1-SNAPSHOT.jar"]