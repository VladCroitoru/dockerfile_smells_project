FROM openjdk:8-jdk-alpine
EXPOSE 4005
VOLUME /main-app
ADD /target/bank-data-service-0.1.0.jar bank-data-service-0.1.0.jar
ENTRYPOINT ["java","-jar","bank-data-service-0.1.0.jar"]