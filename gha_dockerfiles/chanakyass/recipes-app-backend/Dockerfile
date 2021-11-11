# For Java 11, try this
FROM adoptopenjdk/openjdk11:alpine-jre

RUN addgroup -S spring && adduser -S spring -G spring

# Refer to Maven build -> finalName
ARG JAR_FILE=jar/recipes-0.0.1-SNAPSHOT.jar

# cp target/spring-boot-web.jar /opt/app/app.jar
COPY ${JAR_FILE} app.jar

# java -jar /opt/app/app.jar
ENTRYPOINT ["java","-jar","app.jar"]
