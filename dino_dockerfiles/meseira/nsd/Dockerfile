FROM debian:wheezy

MAINTAINER Xavier Gendre "gendre.reivax@gmail.com"

RUN apt-get update && apt-get install -y nsd3

# Prepare and build the empty database
# /etc/nsd3/nsd.conf : configuration file for NSD
# /var/run/nsd3 : allow to create a pidfile for NSD
RUN rm -f /etc/nsd3/nsd.conf && \
    touch /etc/nsd3/nsd.conf && \
    mkdir -p /var/run/nsd3 && \
    zonec -c /etc/nsd3/nsd.conf

# Volumes
# /etc/nsd3 : configuration and zone files
# /var/log/nsd : log files
VOLUME ["/etc/nsd3", "/var/log/nsd"]

EXPOSE 53/udp

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
