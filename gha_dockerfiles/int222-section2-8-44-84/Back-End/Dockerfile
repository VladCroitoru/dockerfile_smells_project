FROM maven AS build
COPY src $PWD/src
COPY pom.xml $PWD
RUN mvn -f $PWD/pom.xml clean package
  
FROM openjdk:16-jdk-alpine
VOLUME /tmp
EXPOSE 3000
COPY --from=build $PWD/target/intregratedbackend-0.0.1-SNAPSHOT.jar app.jar
ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar", "/app.jar"] 