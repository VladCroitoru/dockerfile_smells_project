FROM mwaeckerlin/ubuntu-base
MAINTAINER mwaeckerlin

EXPOSE 2003

RUN apt-get update -y && apt-get install -y graphite-carbon telnet
RUN echo "" >> /etc/carbon/storage-schemas.conf
RUN echo "[icinga2_internals]" >> /etc/carbon/storage-schemas.conf
RUN echo "pattern = ^icinga2\..*\.(max_check_attempts|reachable|current_attempt|execution_time|latency|state|state_type)" >> /etc/carbon/storage-schemas.conf
RUN echo "retentions = 5m:7d" >> /etc/carbon/storage-schemas.conf
RUN echo "" >> /etc/carbon/storage-schemas.conf
RUN echo "[icinga2_default]" >> /etc/carbon/storage-schemas.conf
RUN echo "pattern = ^icinga2\." >> /etc/carbon/storage-schemas.conf
RUN echo "retentions = 1m:7d,5m:14d,30m:90d,360m:4y" >> /etc/carbon/storage-schemas.conf

VOLUME /var/lib/graphite
