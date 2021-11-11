FROM debian:buster

RUN apt-get -qy update && apt-get install -qy \
    live-build \
    time

COPY config /var/livecd
WORKDIR /var/livecd

RUN chmod -R +x auto/ && \
    chmod -R +x config/hooks && \
    chmod +x ./build.sh

VOLUME ["/tmp/builds", "/tmp/logs", "/var/livecd/cache"]

ENTRYPOINT ["time", "./build.sh"]
