FROM alpine:3.4

WORKDIR /
RUN wget -q -O nr.zip http://central.maven.org/maven2/com/newrelic/agent/java/newrelic-java/3.32.0/newrelic-java-3.32.0.zip && \
    unzip nr.zip && rm -f nr.zip
VOLUME /newrelic

CMD true
