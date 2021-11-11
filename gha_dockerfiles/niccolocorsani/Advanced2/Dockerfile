# Start with a base image containing Java runtime
FROM openjdk:11-jre



## Add a volume pointing to /tmp
#VOLUME /tmp

# Make port 8080 available to the world outside this container
EXPOSE 8080


# The application's jar file
ARG JAR_FILE=business-logic-layer/target/operations-backend.jar

# Add the application's jar to the container
ADD ${JAR_FILE} operations-backend.jar

# Run the jar file
#ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/operations-backend.jar"]


ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-Dspring.profiles.active=test1", "-jar","/operations-backend.jar"]


