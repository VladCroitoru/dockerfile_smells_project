FROM openjdk:8u171-alpine3.7
RUN apk --no-cache add curl
COPY build/libs/*-all.jar geometry-ws.jar
CMD java ${JAVA_OPTS} -jar geometry-ws.jar