FROM alpine:latest
MAINTAINER lyc <imyikong@gmail.com>

ADD conf/uwsgi.ini /etc/uwsgi.ini
ADD entry.sh /entry.sh

VOLUME /data/
WORKDIR /

ENV DB_ENGINE django.db.backends.mysql
ENV DB_NAME nerverland
ENV DB_USER nerverland
ENV DB_PASSWORD ""
ENV DB_HOST ""
ENV DB_PORT ""

RUN apk update && \
    apk add git python py-pip uwsgi-python py-mysqldb && \
    git clone --depth 1 https://github.com/MrLYC/neverland.git && \
    pip install -r /neverland/requirements.txt && \
    addgroup www-data && \
    adduser www-data -G www-data -D && \
    apk del git py-pip && \
    rm -rf /var/cache/apk/*

EXPOSE 7581

ENTRYPOINT ["/entry.sh"]
