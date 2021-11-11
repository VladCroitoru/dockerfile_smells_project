FROM alpine:edge
MAINTAINER Philipp A. Baer <github@ph.baer.one>

ENV UID=991 GID=991 \
    SVNWEBDIR=svn

RUN apk add --update s6 su-exec apache2 apache2-utils apache2-webdav apache2-ldap mod_dav_svn subversion && \
    rm /var/cache/apk/* && \
    mkdir /run/apache2 && \
    mkdir /svn

COPY apache2/httpd.conf /etc/apache2/httpd.conf
COPY s6.d  /etc/s6.d
COPY run.sh /usr/local/bin/run.sh

RUN chmod +x /usr/local/bin/run.sh /etc/s6.d/*/* /etc/s6.d/.s6-svscan/*

VOLUME /svn

EXPOSE 8080 3690

CMD ["/usr/local/bin/run.sh"]
#CMD ["/usr/sbin/apachectl", "-DFOREGROUND"]
