FROM openjdk:16-slim

ARG SOURCE_JAR=https://papermc.io/api/v2/projects/paper/versions/1.17.1/builds/349/downloads/paper-1.17.1-349.jar

RUN apt update
RUN apt install -y curl

WORKDIR /app
RUN curl \
  -L \
  -o paper.jar \
  "${SOURCE_JAR}"

ENV JAVA_XMX 1G

COPY ./app/ /app/

ENTRYPOINT ["/app/entrypoint.sh"]
