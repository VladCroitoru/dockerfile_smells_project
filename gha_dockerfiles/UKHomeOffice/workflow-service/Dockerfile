FROM quay.io/ukhomeofficedigital/jre:latest

WORKDIR /app

ADD ./build/libs/workflow-service.jar /app/

USER java

ENTRYPOINT /opt/java/openjdk/bin/java -jar /app/workflow-service.jar

EXPOSE 8080

USER 1000
