FROM openjdk:8-jdk-alpine
ARG WAR_FILE=MyTB-0.0.1-SNAPSHOT.war
COPY ${WAR_FILE} MyTB.war
ENTRYPOINT ["java","-jar", "MyTB.war"]
