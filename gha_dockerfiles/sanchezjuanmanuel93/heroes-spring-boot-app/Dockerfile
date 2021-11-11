FROM openjdk:11
EXPOSE 8080
ADD target/heroes-api.jar heroes-api.jar
ENTRYPOINT ["java","-jar","/heroes-api.jar"]