FROM debian:8
MAINTAINER Antonio Esposito "kobe@befair.it"

ENV DEBIAN_FRONTEND noninteractive
RUN apt update && \
    apt install -y libfontconfig adduser && \
    rm -rf /var/lib/apt/lists/*

COPY grafana.deb /tmp/grafana.deb
RUN dpkg -i /tmp/grafana.deb

COPY conf /etc/grafana/

WORKDIR /usr/share/grafana

EXPOSE 3000
CMD ["/usr/sbin/grafana-server", "--config=/etc/grafana/grafana.ini", "cfg:default.paths.data=/var/lib/grafana", "cfg:default.paths.logs=/var/log/grafana"]
