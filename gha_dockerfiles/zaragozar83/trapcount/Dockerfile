FROM openjdk:8-jdk-alpine
VOLUME /tmp
COPY target/trapcount-1.0.0.jar .
EXPOSE 8080
ENTRYPOINT java $JAVA_OPTS -jar trapcount-1.0.0.jar