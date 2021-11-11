FROM maven:3-jdk-11 AS build
COPY settings-docker.xml /usr/share/maven/ref/
COPY src /usr/src/app/src
COPY pom.xml /usr/src/app
RUN mvn -f /usr/src/app/pom.xml -gs /usr/share/maven/ref/settings-docker.xml -DskipTests clean package

FROM openjdk:11-slim-buster
COPY --from=build /usr/src/app/target/pscload-*.jar /usr/app/pscload.jar
RUN mkdir -p /app/files-repo
RUN chown -R daemon: /app/files-repo
USER daemon
EXPOSE 8080
ENTRYPOINT ["java","-jar","/usr/app/pscload.jar"]
