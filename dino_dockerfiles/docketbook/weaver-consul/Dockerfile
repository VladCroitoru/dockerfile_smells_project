FROM arachnysdocker/athenapdf-service:latest
MAINTAINER Dave Finster <df@docketbook.io>

ENV CONTAINERBUDDY_VERSION 1.2.1

COPY weaver-consul.json /etc/weaver-consul.json
COPY weaver_health.sh /usr/local/bin/weaver_health.sh
COPY entrypoint.sh /athenapdf-service/conf/entrypoint.sh

USER root

RUN set -x \
  && apt-get update \
  && apt-get install -y curl \
  && wget -O containerpilot.tar.gz https://github.com/joyent/containerpilot/releases/download/2.1.2/containerpilot-2.1.2.tar.gz \
  && tar -xzf containerpilot.tar.gz -C /usr/local/bin \
  && rm -r containerpilot.tar.gz \
  && chmod +x /usr/local/bin/weaver_health.sh \
  && apt-get -yq autoremove \
  && apt-get -yq clean \
  && rm -rf /var/lib/apt/lists/* \
  && truncate -s 0 /var/log/*log \
  && chmod +x /athenapdf-service/conf/entrypoint.sh

ENV CONTAINERPILOT=file:///etc/weaver-consul.json

EXPOSE 8080

ENTRYPOINT [ "/usr/local/bin/containerpilot", "/athenapdf-service/conf/entrypoint.sh", "weaver"]
