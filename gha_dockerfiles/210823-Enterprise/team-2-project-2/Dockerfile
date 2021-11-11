FROM openjdk:8-jdk-alpine

COPY /target/team2-backend-0.0.1-SNAPSHOT.war team2-backend-0.0.1-SNAPSHOT.war

EXPOSE 5000

ENTRYPOINT ["java", "-war", "/team2-backend-0.0.1-SNAPSHOT.war"]