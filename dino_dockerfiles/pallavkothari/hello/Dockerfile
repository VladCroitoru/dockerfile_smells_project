# https://github.com/carlossg/docker-maven#multi-stage-builds
# build
FROM maven:alpine as build 
WORKDIR /usr/src/app
COPY pom.xml .
RUN mvn -B -e -C -T 1C org.apache.maven.plugins:maven-dependency-plugin:3.0.2:go-offline
COPY . .
RUN mvn -B -e -o -T 1C verify

# package without maven
FROM openjdk:alpine
COPY --from=build /usr/src/app/target/*.jar ./app.jar

# run the image as a non-root user
RUN adduser -D myuser
USER myuser

CMD java -jar ./app.jar

