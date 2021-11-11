FROM phusion/baseimage:0.9.17

CMD ["/sbin/my_init"]

RUN apt-get update && \
    apt-get install -y postfix postfix-pgsql dovecot-common dovecot-imapd dovecot-pgsql && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /var/vmail
VOLUME /var/vmail
RUN groupadd -g 500 vmail
RUN useradd -g vmail -u 500 vmail -d /var/vmail -m

VOLUME /etc/dovecot
VOLUME /etc/postfix

EXPOSE 25
EXPOSE 465
EXPOSE 143
EXPOSE 993

RUN mkdir /etc/service/postfix && \
    echo "#!/bin/sh\npostfix start && tail -f /var/log/mail.log" > /etc/service/postfix/run && \
    chmod +x /etc/service/postfix/run
RUN mkdir /etc/service/dovecot && \
    echo "#!/bin/sh\ndovecot -F" > /etc/service/dovecot/run && \
    chmod +x /etc/service/dovecot/run
