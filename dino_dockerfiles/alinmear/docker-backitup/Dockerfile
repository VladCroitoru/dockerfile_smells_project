FROM alpine:3.5
MAINTAINER Paul Steinlechner 

ENV GNUPGHOME=/gpg_home TIMEZONE=Europe/Vienna

# RUN sed -i -e 's/v3\.5/edge/g' /etc/apk/repositories 
RUN apk add --no-cache \
    bash \
    pwgen \
    expect \
    dialog \
    duplicity \
    duply \
    openssh-client \
    rsync \
    py-paramiko \
    py-requests \
    py-requests-oauthlib \
    supervisor \
    mysql-client && \
    apk add --virtual tz --no-cache tzdata && \
    cp /usr/share/zoneinfo/$TIMEZONE /etc/localtime && echo $TIMEZONE > /etc/timezone && \
    apk del tz && rm -rf /var/cache/apk/*
    
COPY files/adbackend.py /usr/lib/python2.7/site-packages/duplicity/backends/adbackend.py
COPY files/mysql_backup.sh /usr/bin/mysql_backup
COPY files/duply_setup.sh /usr/bin/duply_setup
COPY files/override_config.sh /usr/bin/override_config
COPY files/entrypoint.sh /entrypoint.sh
COPY files/gpg_set_trust.sh /usr/bin/gpg_set_trust
COPY files/gpg_setup.sh /usr/bin/gpg_setup
COPY files/cron_setup.sh /usr/bin/cron_setup
COPY files/backitup_export.sh /usr/bin/backitup_export

COPY configs/supervisord.conf /etc/supervisord.conf

RUN chmod +x /usr/bin/mysql_backup && \
    chmod +x /usr/bin/duply_setup && \
    chmod +x /usr/bin/override_config && \
    chmod +x /entrypoint.sh && \
    chmod +x /usr/bin/gpg_set_trust && \
    chmod +x /usr/bin/gpg_setup && \
    chmod +x /usr/bin/cron_setup && \
    chmod +x /usr/bin/backitup_export

VOLUME ["/backup", "/backup_source", "/restore", "/gpg_home", "/root/.duply", "/duply_export"]

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/usr/bin/supervisord"]
