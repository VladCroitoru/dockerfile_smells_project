#Use OPENJDK 15 image.
FROM openjdk:15

#Make variable from project jar.
ARG JAR_FILE=build/libs/*.jar

#Copy project directory in the Docker image directory (/app).
COPY ${JAR_FILE} app.jar

#Add listener to the application's port.
EXPOSE $PORT

#Start the app.
ENTRYPOINT ["java", "-jar", "app.jar"]