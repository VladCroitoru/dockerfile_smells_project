FROM debian:latest
MAINTAINER Pierre Cheynier <pierre.cheynier@gmail.com>

RUN apt-get update && apt-get install -y quagga-bgpd && \
    rm -rf /var/lib/apt/lists/* && \
    usermod -a -G quaggavty root
COPY bgpd.conf /etc/quagga/bgpd.conf

EXPOSE 2605 179

ENTRYPOINT ["/usr/sbin/bgpd", "-i", "/var/run/bgpd.pid", "-g", "root", "-u", "root"]
