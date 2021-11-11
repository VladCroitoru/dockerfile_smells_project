FROM debian:jessie

ENV DEBIAN_FRONTEND noninteractive

RUN echo 'deb http://ftp.debian.org/debian jessie-backports main' >> /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends rsyslog && \
    echo "postfix postfix/main_mailer_type string Internet site" > preseed.txt && \
    echo "postfix postfix/mailname string mail.replace.me" >> preseed.txt && \
    debconf-set-selections preseed.txt && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \ 
        postfix \ 
        postfix-mysql \
        postfix-doc \
        dovecot-common \
        dovecot-mysql \
        dovecot-imapd \
        dovecot-pop3d \
        libsasl2-2 \
        libsasl2-modules \
        libsasl2-modules-sql \
        sasl2-bin libpam-mysql \
        opendkim \
        opendkim-tools && \
    apt-get -t jessie-backports -y install postsrsd && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /usr/share/locale/* && \
    rm -rf /usr/share/man/* && \
    rm -rf /usr/share/doc/* && \
    mkdir -p /etc/postfix/tls
    
COPY docker-entrypoint.sh /usr/local/bin/
COPY run-postfix.sh /opt/postfix/
COPY conf /opt/postfix/conf

ENV MAIL_HOST_NAME MAIL_FQDN MAIL_DOMAIN POSTFIX_DB_HOST POSTFIX_DB_NAME POSTFIX_DB_USER POSTFIX_DB_PASSWORD

VOLUME /etc/postfix/tls
VOLUME /etc/mail/dkim
VOLUME /var/mail/vmail
VOLUME /opt/postfix/conf/postsrsd/secret

EXPOSE 25 587

WORKDIR /opt/postfix/

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["/opt/postfix/run-postfix.sh"]
