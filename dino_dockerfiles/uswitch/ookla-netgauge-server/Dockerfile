FROM debian:jessie

WORKDIR /var/www

RUN apt-get update && \
    apt-get install -y wget && \
    rm -rf /var/lib/apt/lists/*

# https://www.ookla.com/support/a22705918/NetGauge-Linux-Unix-Server-Daemon-Installation
RUN wget http://install.speedtest.net/ooklaserver/ooklaserver.sh && \
    chmod a+x ooklaserver.sh && \
    ./ooklaserver.sh install -f

# Expose the default port
EXPOSE 8080 5060

CMD ["./OoklaServer", "start"]
