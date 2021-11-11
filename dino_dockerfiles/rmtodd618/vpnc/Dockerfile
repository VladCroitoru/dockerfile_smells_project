FROM debian:jessie

CMD ["/etc/service/vpnc/run"]

RUN apt-get update -y && apt-get install -y vpnc

# Setup vpnc service
RUN mkdir -p /etc/service/vpnc
COPY bin/vpnc.sh /etc/service/vpnc/run

# Clean up
RUN apt-get autoremove -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*