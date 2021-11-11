#FROM ubuntu:latest
FROM java:8

RUN mkdir /opt/diff-info-service/
COPY build/libs/diff-info-service-0.1.0-SNAPSHOT-capsule.jar /opt/diff-info-service/
CMD ["java", "-jar", "/opt/diff-info-service/diff-info-service-0.1.0-SNAPSHOT-capsule.jar", "server"]