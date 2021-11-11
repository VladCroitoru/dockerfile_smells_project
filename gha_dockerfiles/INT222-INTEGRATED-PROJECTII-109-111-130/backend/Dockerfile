#FROM maven AS build
#RUN sudo apt install maven
#RUN mvn -f $PWD/pom.xml clean package
#RUN  pwd  mvn clean package
# Use official base image of Java Runtim
FROM maven AS MAVENS
COPY pom.xml /build/
COPY src /build/src/
WORKDIR /build/
RUN  mvn clean package

FROM openjdk:16-jdk-alpine
# FROM adoptopenjdk/openjdk11:latest
# Set volume point to /tmp

VOLUME /tmp
# WORKDIR /tmp
# RUN mkdir /tmp/product-images
# Make port 8080 available to the world outside container
EXPOSE 3000

#RUN pwd /mvnw package

# Set application's JAR file
# ARG JAR_FILE=MAVENS /build/target/int222-0.0.1-SNAPSHOT.jar
COPY --from=MAVENS /build/target/int222-0.0.1-SNAPSHOT.jar /usr/local/lib/int222-0.0.1-SNAPSHOT.jar
# Add the application's JAR file to the container
# ADD ${JAR_FILE} app.jar


# Run the JAR file
ENTRYPOINT ["java", "-jar", "/usr/local/lib/int222-0.0.1-SNAPSHOT.jar"]

