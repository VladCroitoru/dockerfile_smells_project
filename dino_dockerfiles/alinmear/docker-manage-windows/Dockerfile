FROM alpine:3.5

MAINTAINER Paul Steinlechner 

ENV TIMEZONE=Europe/Vienna MANAGEWINDOWS_CRON='0 3 * * *' \
    MANAGEWINDOWS_DOMAIN="DOMAIN.LOC" MANAGEWINDOWS_KDC="kdc.domain.loc" \
    MANAGEWINDOWS_USER="administrator" MANAGEWINDOWS_PASS="mypass"

RUN apk --update add bash supervisor python py-pip openssl ca-certificates krb5 krb5-libs && \
    apk --update add --virtual build-dependencies \
    python-dev libffi-dev openssl-dev build-base tzdata \
    krb5-dev && \
    pip install --upgrade pip cffi && \
    pip install ansible==2.2.2 pywinrm[kerberos] && \
    cp /usr/share/zoneinfo/$TIMEZONE /etc/localtime && echo $TIMEZONE > /etc/timezone && \
    apk del build-dependencies && rm -rf /var/cache/apk/*

COPY files/entrypoint.sh /entrypoint.sh
COPY files/supervisord.conf /etc/supervisord.conf
COPY files/execute_playbook.sh /usr/bin/execute_playbook

RUN chmod +x /entrypoint.sh /usr/bin/execute_playbook

VOLUME ["/opt/manage-windows"]

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/usr/bin/supervisord"]
