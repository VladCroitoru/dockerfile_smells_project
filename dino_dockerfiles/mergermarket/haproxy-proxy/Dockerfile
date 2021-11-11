FROM haproxy:latest

RUN apt-get update && apt-get install -y cron rsyslog && \
    sed -i 's/#$ModLoad imudp/$ModLoad imudp/g' /etc/rsyslog.conf && \
    sed -i 's/#$UDPServerRun 514/$UDPServerRun 514/g' /etc/rsyslog.conf && \
    apt-get clean

COPY haproxy.conf /etc/rsyslog.d/
COPY docker-entrypoint.sh /
COPY log_rotate /etc/cron.hourly/

COPY haproxy.cfg /usr/local/etc/haproxy/

ENTRYPOINT ["/docker-entrypoint.sh"]
