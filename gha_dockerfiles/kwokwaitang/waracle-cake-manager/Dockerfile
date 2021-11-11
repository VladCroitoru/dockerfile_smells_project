# To build a Docker image with the Cake Manager application (main branch)...
# docker build -t cake-manager:spring-boot-main-branch .

# To run the application in its own container...
# docker run -p 8080:8080 -p 8443:8443 -p 80:80 cake-manager:spring-boot-main-branch

FROM openjdk:11

# To avoid using root to start-up the application
RUN addgroup -gid 1000 spring
RUN adduser --home /home/spring -uid 1001 --gid 1000 --disabled-password spring

# User spring (from the spring group) will run the application
USER spring:spring

ARG JAR_FILE=target/*.jar
COPY ${JAR_FILE} cake-manager.jar
ENTRYPOINT ["java", "-jar", "/cake-manager.jar"]

# https://spring.io/guides/gs/spring-boot-docker/