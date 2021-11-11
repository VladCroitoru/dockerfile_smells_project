FROM openjdk:11.0.7-jre-slim

ENV TZ America/Sao_Paulo
EXPOSE 8080

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV JAVA_TOOL_OPTIONS -Dfile.encoding=UTF8

COPY ./target/lixt-backend-0.0.1-SNAPSHOT.jar /home/lixt-backend.jar
CMD ["java", "-jar", "-Dspring.profiles.active=prod", "/home/lixt-backend.jar"]
