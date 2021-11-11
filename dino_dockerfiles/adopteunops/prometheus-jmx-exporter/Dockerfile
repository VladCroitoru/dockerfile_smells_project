FROM ubuntu:16.04

RUN apt-get update && \
    apt-get -y install curl jq && \
    apt-get clean -q

ENV JMX_VERSION 0.10
ENV JMX_EXPORTER_URL http://central.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/${JMX_VERSION}/jmx_prometheus_javaagent-${JMX_VERSION}.jar
ENV CUSTOM_JMX_CONF_COMMAND ""

ADD startup.sh /usr/bin/startup.sh
ADD configs /etc/jmx_exporter

RUN curl -l ${JMX_EXPORTER_URL} > /etc/jmx_exporter/jmx_exporter_agent.jar

VOLUME /etc/jmx_exporter

CMD ["/usr/bin/startup.sh"]
