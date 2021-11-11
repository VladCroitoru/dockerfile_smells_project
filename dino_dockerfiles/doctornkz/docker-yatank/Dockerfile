# flapi docker
#
# VERSION 0.2
# Based on https://github.com/RiftBit/docker-yatank by ErgoZ,
# but uses PyPI Tank package instead of .deb

FROM ubuntu:precise
MAINTAINER Alexey Lavrenuke <direvius@yandex-team.ru>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y -q --no-install-recommends python-software-properties software-properties-common && \
    add-apt-repository ppa:yandex-load/main -y && \
    apt-get update && apt-get install -y -q phantom phantom-ssl && \
    mkdir /yandex-example-configs && \
    mkdir /yandex-tank-configs

RUN apt-get install -y -q python-pip python-dev

RUN pip install yandextank && pip install yatank-online

RUN echo "net.ipv4.tcp_max_tw_buckets=65536" >> /etc/sysctl.conf && \
    echo "net.ipv4.tcp_tw_recycle=1" >> /etc/sysctl.conf && \
    echo "net.ipv4.tcp_tw_reuse=0" >> /etc/sysctl.conf && \
    echo "net.ipv4.tcp_max_syn_backlog=131072" >> /etc/sysctl.conf && \
    echo "net.ipv4.tcp_syn_retries=3" >> /etc/sysctl.conf && \
    echo "net.ipv4.tcp_synack_retries=3" >> /etc/sysctl.conf && \
    echo "net.ipv4.tcp_retries1=3" >> /etc/sysctl.conf && \
    echo "net.ipv4.tcp_retries2=8" >> /etc/sysctl.conf && \
    echo "net.ipv4.tcp_rmem=16384 174760 349520" >> /etc/sysctl.conf && \
    echo "net.ipv4.tcp_wmem=16384 131072 262144" >> /etc/sysctl.conf && \
    echo "net.ipv4.tcp_mem=262144 524288 1048576" >> /etc/sysctl.conf && \
    echo "net.ipv4.tcp_max_orphans=65536" >> /etc/sysctl.conf && \
    echo "net.ipv4.tcp_fin_timeout=10" >> /etc/sysctl.conf && \
    echo "net.ipv4.tcp_low_latency=1" >> /etc/sysctl.conf && \
    echo "net.ipv4.tcp_syncookies=0" >> /etc/sysctl.conf

COPY docker-entrypoint.sh /entrypoint.sh
COPY example-load.ini /yandex-example-configs/load.ini

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 8888/tcp 8001/tcp

CMD ["-c /yandex-example-configs/load.ini"]
