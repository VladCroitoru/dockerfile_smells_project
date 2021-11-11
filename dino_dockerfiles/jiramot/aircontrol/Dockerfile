FROM ubuntu:16.04

RUN apt-get update && apt-get install -qq default-jdk iperf expect

ADD https://dl.ubnt.com/aircontrol2/aircontrol-v2.0.1.2325.170130.0936-unix64.bin /tmp/aircontrol.bin
ADD script.exp /tmp/script.exp

RUN cd /tmp && \
    chmod u+x script.exp && \
    chmod u+x aircontrol.bin && \
    ./script.exp

RUN mkdir -p /var/log/aircontrol2 && \
    touch /var/log/aircontrol2/server.log

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 9081 5432
ENTRYPOINT service postgresql-9.5 start && \
            service airControl2Server start && \
            tail -f /var/log/aircontrol2/server.log
