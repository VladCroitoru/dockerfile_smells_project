FROM silarsis/docker-proxy:latest

ENV LOGGER_IP 127.0.0.1

RUN apt-get update
RUN apt-get install -y squidclient

COPY squid.conf /etc/squid3/squid.conf
COPY configure_and_start_squid.sh /usr/local/bin/configure_and_start_squid.sh

CMD ["/usr/local/bin/configure_and_start_squid.sh"]

