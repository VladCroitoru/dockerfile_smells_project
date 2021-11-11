FROM mesosphere/marathon-lb
ENV KAFKA_TOPIC=haproxy_logs PORTS=9090
RUN apt-get update \
  && apt-get install -y --no-install-recommends curl rsyslog-kafka \
  && rm -rf /var/lib/apt/lists/* \
  && mkdir -p /var/state/haproxy /var/run/haproxy
COPY rsyslog /marathon-lb/service/rsyslog
