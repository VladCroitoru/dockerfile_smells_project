FROM openjdk:11-jre-slim

LABEL NSD <support@nsd.no>

ENV PROFILE=stage
EXPOSE 5001
VOLUME /home/deploy/deployment/test/uploads-to-qddt/

COPY ./build/libs/QDDT.jar /QDDT.jar

ENTRYPOINT exec java $JAVA_OPTS -jar /QDDT.jar
