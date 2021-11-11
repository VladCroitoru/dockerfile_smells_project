FROM debian:stretch

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -yqq pdns-backend-sqlite3 && \
    apt-get clean && \
    apt-get -yqq autoremove && \
    rm -rf /var/lib/apt/lists/*

RUN rm -f /etc/powerdns/pdns.d/pdns.simplebind.conf

COPY pdns.conf /etc/powerdns/pdns.conf

EXPOSE 53/udp 53/tcp 8081/tcp

CMD ["pdns_server", "--daemon=no"]
