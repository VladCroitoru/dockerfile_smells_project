FROM debian:stretch

RUN apt-get update && apt-get install -y bitlbee-libpurple && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 6667

VOLUME /var/lib/bitlbee

ADD entrypoint.sh /usr/local/bin/entrypoint.sh
ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]
