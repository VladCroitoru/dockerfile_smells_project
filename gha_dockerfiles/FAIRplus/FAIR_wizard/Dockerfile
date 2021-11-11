FROM openjdk:11-jre
ARG JAR_FILE=target/*.jar
COPY ${JAR_FILE} fair-wizard.jar
ENTRYPOINT ["java","-jar","/fair-wizard.jar", "--spring.profiles.active=docker"]
