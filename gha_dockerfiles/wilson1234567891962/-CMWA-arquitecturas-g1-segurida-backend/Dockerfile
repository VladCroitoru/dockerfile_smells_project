FROM openjdk:8
EXPOSE 8082
ADD log4j.properties log4j.properties
ADD target/login.management.jar login.management.jar
ENTRYPOINT ["java","-jar","/login.management.jar"]
