#FROM openjdk:8-jdk
FROM mesosphere/mesos:1.1.0-2.0.107.ubuntu1404
RUN apt-get update -qq && apt-get install -y wget
RUN wget -q https://github.com/twosigma/Cook/releases/download/v1.0.0/cook-1.0.0-standalone.jar
RUN wget -q https://raw.githubusercontent.com/twosigma/Cook/master/scheduler/dev-config.edn
ENV CONF_PATH /dev-config.edn
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
