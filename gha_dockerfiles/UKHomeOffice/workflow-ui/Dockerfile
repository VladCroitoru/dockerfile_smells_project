FROM quay.io/ukhomeofficedigital/jre:latest

WORKDIR /app

ADD ./server/build/libs/workflow-ui.jar /app/

USER java

ENTRYPOINT /opt/java/openjdk/bin/java -jar /app/workflow-ui.jar

EXPOSE 8080

USER 1000
