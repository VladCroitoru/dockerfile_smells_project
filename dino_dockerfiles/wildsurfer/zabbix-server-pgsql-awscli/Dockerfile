FROM zabbix/zabbix-server-pgsql:alpine-3.2.1
RUN apk --no-cache add groff less python py-pip && \
        pip --no-cache-dir install awscli && \
        rm -rf /var/cache/apk/*
COPY ./alertscripts/ /usr/lib/zabbix/alertscripts
