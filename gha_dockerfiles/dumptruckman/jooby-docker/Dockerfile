FROM openjdk:17-slim

RUN apt-get update && apt-get upgrade && apt-get install -y wget unzip

RUN mkdir -p /opt/jooby

RUN wget https://repo1.maven.org/maven2/io/jooby/jooby-cli/2.11.0/jooby-cli-2.11.0.zip

RUN unzip jooby-cli-2.11.0.zip -d /opt/jooby \
  && chmod +x /opt/jooby/bin/jooby \
  && mkdir /opt/jooby/run \
  && chmod -R a+rwx /opt/jooby/run

WORKDIR /tmp/project

RUN /opt/jooby/bin/jooby set -w /tmp/project

ENTRYPOINT ["/opt/jooby/bin/jooby"]
