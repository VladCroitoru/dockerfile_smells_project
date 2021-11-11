FROM openjdk:11 as build
ADD target/rest-test-0.0.1-SNAPSHOT.jar .
EXPOSE 8000
CMD []
ENTRYPOINT ["java", "-Dspring.profiles.active-prod", "-jar", "rest-test-0.0.1-SNAPSHOT.jar"]

