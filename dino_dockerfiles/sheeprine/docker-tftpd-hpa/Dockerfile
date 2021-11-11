FROM debian:jessie

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    tftpd-hpa \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

VOLUME /var/lib/tftpboot

EXPOSE 69/udp
CMD in.tftpd -L --user tftp -a 0.0.0.0:69 -s -B1468 -v /var/lib/tftpboot
