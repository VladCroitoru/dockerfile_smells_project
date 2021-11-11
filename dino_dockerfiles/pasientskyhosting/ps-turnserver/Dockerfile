FROM debian:buster-slim
MAINTAINER Andreas Krüger <ak@patientsky.com>

ENV TINI_VERSION v0.18.0
COPY bin/* /
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini

RUN apt-get update && apt-get dist-upgrade -y && \
 apt-get update -y && \
 # apt-get install coturn net-tools supervisor rsyslog -y && \
 apt-get install coturn net-tools -y && \
 apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
 chmod +x /metrics.sh && \
 chmod +x /turnserver.sh && \
 chmod +x /tini

COPY conf/* /etc/
#COPY conf/logrotate.d/* /etc/logrotate.d/


EXPOSE 3478/udp
EXPOSE 49152-65000/udp

ENTRYPOINT ["/tini", "--"]

#CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]
CMD ["/turnserver.sh"]
