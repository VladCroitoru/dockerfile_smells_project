FROM debian:jessie


MAINTAINER Juan Ramon Alfaro <jralfaro@oondeo.es>


ENV SLAPD_VERSION=2.4.40 \
    FUSIONDIRECTORY_DEB_PKG_VERSION=1.0.9.3-1


RUN export DEBIAN_FRONTEND=noninteractive && \
    export LC_ALL=es_ES.UTF-8 && \
    export LANG=C && \
    export LANGUAGE=C && \
    apt-get update && \
    apt-get install -y --no-install-recommends gnupg && \
    gpg --keyserver keys.gnupg.net --recv-keys E184859262B4981F && \
    gpg -a --export E184859262B4981F | apt-key add - && \
    echo 'deb http://repos.fusiondirectory.org/debian-jessie jessie main' > /etc/apt/sources.list.d/fd.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends slapd=${SLAPD_VERSION}* ldap-utils dialog locales schema2ldif \
        fusiondirectory-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-alias-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-apache2-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-applications-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-argonaut-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-autofs-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-cyrus-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-debconf-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-dhcp-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-dns-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-dovecot-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-dsa-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-ejbca-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-fai-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-freeradius-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-fusioninventory-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-gpg-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-ipmi-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-kolab2-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-mail-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-nagios-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-netgroups-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-opsi-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-personal-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-ppolicy-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-puppet-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-pureftpd-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-quota-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-repository-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-samba-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-sogo-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-squid-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-ssh-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-sudo-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-supann-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-sympa-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-systems-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-weblink-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* \
        fusiondirectory-plugin-webservice-schema=${FUSIONDIRECTORY_DEB_PKG_VERSION}* && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    echo "es_ES.UTF-8 UTF-8" >> /etc/locale.gen && \
    dpkg-reconfigure locales


RUN mv /etc/ldap /etc/ldap.dist

EXPOSE 389

VOLUME ["/etc/ldap", "/var/lib/ldap"]

COPY modules/ /etc/ldap.dist/modules

COPY entrypoint.sh /entrypoint.sh

COPY schema.sh /schema.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["slapd", "-d", "32768", "-u", "openldap", "-g", "openldap","-h" ,'ldap:/// ldapi:///']
