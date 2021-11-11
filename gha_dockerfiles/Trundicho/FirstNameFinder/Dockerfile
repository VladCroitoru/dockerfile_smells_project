FROM adoptopenjdk:11-jre-hotspot
EXPOSE 8080
ARG JAR_FILE=target/firstNameFinder-0.0.1-SNAPSHOT.war
ADD ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]