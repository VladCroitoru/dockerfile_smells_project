FROM java:8-jre

MAINTAINER Alexey Kupershtokh <alexey.kupershtokh@gmail.com>

ENV LOGSTASH_VERSION 1.5.0-rc3

RUN curl -s "https://download.elastic.co/logstash/logstash/logstash-${LOGSTASH_VERSION}.tar.gz" | \
    tar xz -C /opt && \
    mv "/opt/logstash-${LOGSTASH_VERSION}" /opt/logstash

RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/moshen/logstash-http-input.git /tmp/logstash-http-input \
    && cd /tmp/logstash-http-input \
    && ./gradlew install -PinstallDir=/opt/logstash \
    && ln -s /opt/logstash/plugins/logstash/inputs/http.rb /opt/logstash/lib/logstash/inputs/http.rb \
    && rm -rf /tmp/logstash-http-input

ENTRYPOINT ["/opt/logstash/bin/logstash"]

CMD ["-f", "/etc/logstash/conf.d/"]
