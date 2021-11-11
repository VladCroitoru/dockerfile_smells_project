#
# Stage 'dist' creates project distribution.
#
# https://hub.docker.com/_/maven

FROM maven:3-jdk-10 AS dist
USER root
COPY / /app
WORKDIR /app
RUN mvn -Duser.home=/app package

#
# Stage 'runtime' creates final Docker image to use in runtime.
#
# https://hub.docker.com/_/tomcat
FROM openjdk:latest AS runtime
COPY --from=dist /app/target/guestblog.jar /opt/guestblog/
EXPOSE 8080 8080
CMD exec java $JAVA_CMD_ARGS -jar /opt/guestblog/guestblog.jar
