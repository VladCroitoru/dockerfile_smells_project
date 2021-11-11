FROM analogic/trusty
MAINTAINER info@analogic.cz

RUN echo 'deb http://archive.ubuntu.com/ubuntu/ trusty multiverse' >> /etc/apt/sources.list && \
    echo 'deb http://archive.ubuntu.com/ubuntu/ trusty-updates multiverse' >> /etc/apt/sources.list && \
    echo 'deb http://archive.ubuntu.com/ubuntu/ trusty-security multiverse' >> /etc/apt/sources.list && \
    apt-get update && apt-get upgrade -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends cron cacti cacti-spine snmp-mibs-downloader

VOLUME ["/var/lib/cacti/rra/", "/var/log"]
ADD rootfs /
EXPOSE 80


