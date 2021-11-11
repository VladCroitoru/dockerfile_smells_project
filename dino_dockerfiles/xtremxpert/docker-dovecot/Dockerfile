FROM ubuntu:latest

# default config
ENV DBHOST=dbsrv \
    DBUSER=mailuser \
    DBNAME=mailserver \
    DBPASS=Ch4ng3m3

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update \
    && apt-get install -y \
        dovecot-antispam \
        dovecot-common \
        dovecot-imapd \
        dovecot-lmtpd \
        dovecot-managesieved \
        dovecot-mysql \
        dovecot-sieve \
        python-pip \
        spamc \
    && pip install envtpl
    
COPY dovecot /etc/dovecot
COPY bin /usr/local/bin  

VOLUME /var/mail /var/lib/dovecot /etc/letsencrypt
# IMAP ports  
EXPOSE 143 993 4190

CMD sh /usr/local/bin/startup.sh
