FROM maven:3.8.3-openjdk-17 AS MAVEN_BUILD
COPY pom.xml /build/
COPY src /build/src/
# COPY ./src/main/resources/app.yml /build/src/main/resources/application.yml
WORKDIR /build/
RUN mvn package -Dmaven.test.skip=true
FROM openjdk:17-alpine
WORKDIR /root
EXPOSE 80
COPY --from=MAVEN_BUILD /build/target/push.jar /root/push.jar
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/urandom","-jar", "push.jar"]