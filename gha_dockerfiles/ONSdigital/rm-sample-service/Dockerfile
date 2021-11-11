FROM openjdk:11-jre-slim

RUN apt-get update
COPY target/samplesvc.jar /opt/samplesvc.jar

ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS -jar /opt/samplesvc.jar" ]
