FROM debian:jessie

RUN apt-get update && \
    apt-get install -y fio && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY README.md /README
COPY entrypoint.sh /entrypoint
COPY fio /fio

WORKDIR /fio

ENTRYPOINT ["/entrypoint"]

