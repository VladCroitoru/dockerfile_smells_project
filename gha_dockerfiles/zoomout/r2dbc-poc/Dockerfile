FROM openjdk:14-jdk-alpine
VOLUME /tmp
ARG JAR_FILE=build/libs/*.jar
COPY ${JAR_FILE} app.jar
RUN mkdir -p /home/docker/app/
RUN echo "java \$@ -jar -Dreactor.netty.http.server.accessLogEnabled=true /app.jar" > /home/docker/app/entrypoint.sh
ENTRYPOINT ["/bin/sh", "/home/docker/app/entrypoint.sh"]
