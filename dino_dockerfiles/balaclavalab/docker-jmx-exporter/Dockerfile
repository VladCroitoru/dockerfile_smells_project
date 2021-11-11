FROM openjdk:14-ea-jdk-alpine3.10

ENV JMX_EXPORTER=0.12.0

EXPOSE 8080

RUN apk add wget --no-cache \
  && mkdir -p /opt/jmx_prometheus_httpserver \
  && wget http://central.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_httpserver/${JMX_EXPORTER}/jmx_prometheus_httpserver-${JMX_EXPORTER}-jar-with-dependencies.jar \
          -O /opt/jmx_prometheus_httpserver/jmx_prometheus_httpserver.jar

ENTRYPOINT ["java", "-jar"]
CMD ["/opt/jmx_prometheus_httpserver/jmx_prometheus_httpserver.jar"]
