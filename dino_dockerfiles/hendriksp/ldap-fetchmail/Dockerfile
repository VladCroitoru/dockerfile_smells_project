FROM alpine:3.4
MAINTAINER Hendrik Spohr <hendrik.spohr@gmx.net>

RUN set -e \
  && apk add --no-cache fetchmail openldap-clients ca-certificates

USER fetchmail

COPY ldap-fetchmail /usr/local/bin/ldap-fetchmail
COPY make-fetchmailrc /usr/local/bin/make-fetchmailrc
COPY entrypoint.sh /entrypoint.sh

VOLUME /var/fetchmail

ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "ldap-fetchmail" ]
