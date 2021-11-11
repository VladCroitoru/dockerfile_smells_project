# put /bin/sh scripts in /etc/periodic/{15min|hourly|daily|weekly|monthly}

FROM alpine:3.4
MAINTAINER Hubert Chathi <hubert@muchlearning.org>

RUN apk add --update openssl ca-certificates \
    && rm -rf /var/cache/apk/* \
    && wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.1.1/dumb-init_1.1.1_amd64 \
    && chmod +x /usr/local/bin/dumb-init \
    && wget -O /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v1.3.4/bin/linux/amd64/kubectl \
    && chmod +x /usr/local/bin/kubectl

COPY run-sh-parts /usr/local/bin/
COPY crontab /var/spool/cron/crontabs/root
CMD ["/usr/local/bin/dumb-init", "-c", "/usr/sbin/crond", "-d", "7", "-f"]
