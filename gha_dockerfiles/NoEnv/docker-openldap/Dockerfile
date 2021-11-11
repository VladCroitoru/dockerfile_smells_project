FROM alpine:3.14

LABEL maintainer "NoEnv"
LABEL version "2.4.59"
LABEL description "OpenLDAP as Docker Image"

ARG lang="en_US.UTF-8"
ARG backend="mdb"
ARG version="2.4.59-r3"

ENV LANG "${lang}"
ENV USER "ldap"
ENV GROUP "$USER"

ADD openssh-lpk.schema /etc/openldap/schema/openssh-lpk.schema
ADD entrypoint.sh /usr/local/bin/entrypoint.sh
RUN apk add --no-cache --purge --clean-protected -u ca-certificates openldap=$version \
    openldap-clients openldap-overlay-ppolicy openldap-overlay-unique openldap-back-$backend \
 && mkdir /run/openldap \
 && chown $USER.$GROUP /run/openldap \
 && rm -rf /var/cache/apk/*

EXPOSE 389 636

ENTRYPOINT [ "entrypoint.sh" ]
