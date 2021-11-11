# Build stage
FROM gradle:jdk11 AS build
COPY src /home/app/src
COPY settings.gradle /home/app
COPY build.gradle /home/app
RUN cd /home/app && gradle bootJar

#
# Package stage
#
FROM openjdk:11-jre-slim-buster
WORKDIR /workffice/
COPY --from=build /home/app/build/libs/*.jar ./app.jar
ENV PORT 8080
CMD ["java", "-Dserver.port=${PORT}", "-jar" , "./app.jar", "--spring.config.location=classpath:/prod_application.properties"]
