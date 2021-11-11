FROM gliderlabs/alpine:latest
MAINTAINER Wisicn <wisicn@gmail.com>

RUN apk-install  python3 curl supervisor \
    && curl -o /master.zip -Lk https://github.com/aploium/shootback/archive/master.zip \
    && mkdir -p /opt/ \
    && unzip -d /opt /master.zip \
    && mkdir -p /etc/supervisor.d/

COPY data/shootbacks.ini /etc/supervisor.d/
VOLUME /etc/supervisor.d
EXPOSE 10022 10023

ENTRYPOINT ["supervisord", "--nodaemon", "--configuration", "/etc/supervisord.conf"]
