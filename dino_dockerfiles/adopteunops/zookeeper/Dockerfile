FROM rawmind/alpine-zk:3.4.9-3

ADD jmx_exporter.yml /tmp/jmx_exporter.yml
RUN curl -L http://repo1.maven.org/maven-central/io/prometheus/jmx/jmx_prometheus_javaagent/0.10/jmx_prometheus_javaagent-0.10.jar -o /tmp/jmx_prometheus_javaagent-0.10.jar
