FROM ubuntu:14.04.3

MAINTAINER khiraiwa

ENV AWS_ACCESS_KEY_ID YOUR_AWS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY YOUR_AWS_SECRET_KEY

COPY kernel/etc /etc

# Install td-agent
RUN \
  apt-get install curl  --no-install-recommends -y && \
  curl --insecure -L https://toolbelt.treasuredata.com/sh/install-ubuntu-trusty-td-agent2.sh | sh && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# Install td-agent plugin
RUN \
  /opt/td-agent/embedded/bin/fluent-gem install fluent-plugin-cloudwatch fluent-plugin-elasticsearch

COPY td-agent/etc/td-agent/td-agent.conf td-agent.conf

VOLUME ["/etc/td-agent"]
EXPOSE 9880/tcp 5170/tcp 5160/udp 24224/tcp 24224/udp

CMD \
  if [ ! -e /etc/td-agent/td-agent.conf ]; then \
    cp /td-agent.conf /etc/td-agent/td-agent.conf; \
    rm -f /td-agent.conf; \
  fi && \
  sed -i -e"s|ELASTICSEARCH_HOST|${ELASTICSEARCH_HOST}|g" /etc/td-agent/td-agent.conf && \
  sed -i -e"s|YOUR_AWS_KEY_ID|${AWS_ACCESS_KEY_ID}|g" /etc/td-agent/td-agent.conf && \
  sed -i -e"s|YOUR_AWS_SECRET_KEY|${AWS_SECRET_ACCESS_KEY}|g" /etc/td-agent/td-agent.conf && \
  service td-agent start && \
  tail -100f /var/log/td-agent/td-agent.log
