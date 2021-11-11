FROM alpine

MAINTAINER packeteer <@gmail.com>

RUN apk add --no-cache openldap openldap-clients openldap-back-hdb openldap-back-bdb ldapvi

EXPOSE 389 636

CMD ["slapd","-d 256","-u ldap","-g ldap","-F /etc/openldap/slapd.d"
