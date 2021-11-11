FROM alpine:3.4
MAINTAINER Hendrik Spohr <hendrik.spohr@gmx.net>

ENV OPENLDAP_VERSION 2.4.44-r1

RUN set -e \
  && apk add --no-cache openldap=$OPENLDAP_VERSION openldap-clients \
  && rm -f /var/lib/openldap/openldap-data/DB_CONFIG.example \
  && rm -f /etc/openldap/DB_CONFIG.example \
  && rm -f /etc/openldap/ldap.conf \
  && rm -f /etc/openldap/ldap.conf.default \
  && rm -f /etc/openldap/slapd.conf \
  && rm -f /etc/openldap/slapd.conf.default \
  && rm -f /etc/openldap/slapd.ldif \
  && rm -f /etc/openldap/slapd.ldif.default

RUN chown -R ldap.ldap /var/lib/openldap

COPY schema_to_ldif.sh /usr/local/sbin/schema_to_ldif
COPY restore.sh /usr/local/sbin/restore
COPY backup.sh /usr/local/sbin/backup
COPY entrypoint.sh /usr/local/sbin/entrypoint.sh

RUN set -e \
  && chmod 755 /usr/local/sbin/schema_to_ldif \
  && chmod 755 /usr/local/sbin/restore \
  && chmod 755 /usr/local/sbin/backup \
  && chmod 755 /usr/local/sbin/entrypoint.sh

VOLUME \
  /in \
  /init \
  /backup \
  /etc/openldap/slapd.d \
  /var/lib/openldap/openldap-data

EXPOSE 389 636

ENTRYPOINT [ "entrypoint.sh" ]

CMD [ "-h", "ldap://0.0.0.0" ]
