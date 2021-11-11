#
# Build stage
#
FROM maven:3.8.2-openjdk-16 AS build
COPY src /home/app/src
COPY pom.xml /home/app
RUN mvn -f /home/app/pom.xml clean package

#
# Package stage
#
FROM adoptopenjdk/openjdk16:alpine
COPY --from=build /home/app/target/*.jar /usr/local/lib/app.jar

EXPOSE 8080

ENTRYPOINT ["java","-jar","/usr/local/lib/app.jar"]