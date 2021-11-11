# Start with a base image containing Java runtime
FROM adoptopenjdk/openjdk16:ubi

# Add Maintainer Info
LABEL maintainer="Aditya Jadhav"

ENV APP_HOME=/usr/app/

ENV JAR_FILE=build/libs/kube-demo-0.0.1-SNAPSHOT.jar

WORKDIR $APP_HOME

#COPY build.gradle settings.gradle gradlew $APP_HOME
#COPY gradle $APP_HOME/gradle
#RUN ./gradlew build

COPY . $APP_HOME

RUN chmod +x gradlew

RUN ./gradlew build

RUN mv build/libs/demo-0.0.1-SNAPSHOT.jar nc-state-dining.jar 

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run the jar file 
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","nc-state-dining.jar"]