# NOT USED AT THE MOMENT

#
# Build stage
#
FROM maven:3.8.1-openjdk-8-slim AS build
WORKDIR /home/app
COPY src src
COPY .mvn .mvn
COPY mvnw pom.xml local-settings.xml ./
RUN mvn -f pom.xml clean package

#
# Package stage
#
FROM openjdk:8-jre-slim
COPY --from=build /home/app/target/tradium-alerts-0.0.1-SNAPSHOT.jar /usr/local/lib/tradium-alerts.jar
EXPOSE 8080

CMD java -Dserver.port=$PORT -jar "/usr/local/lib/tradium-alerts.jar"