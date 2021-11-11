
# Build jar file
FROM maven:3.8.1-openjdk-15 AS build
COPY src /server-mangaclawers/src
COPY pom.xml /server-mangaclawers/
RUN mvn package -f /server-mangaclawers/pom.xml -D
# RUN mvn package -f /server-mangaclawers/pom.xml -Denv01=val01 -Denv02=val02  >>  add env variable


# run jar file
FROM openjdk:15-jdk-alpine
COPY --from=build /server-mangaclawers/target/server-api-0.0.1-SNAPSHOT.jar server-mangaclawers.jar
EXPOSE 4000
ENTRYPOINT ["java", "-jar", "server-mangaclawers.jar"]


# If want to build and run only this Dockerfile instead of docker compose, add local.env file when run >>> follow below
## docker build -t server-mangaclawers .
## docker run --rm -it --env-file src/local.env server-mangaclawers:latest