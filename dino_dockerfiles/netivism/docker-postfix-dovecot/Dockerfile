FROM debian:buster
MAINTAINER Jimmy Huang <jimmy@netivism.com.tw>

ENV DEBIAN_FRONTEND noninteractive

RUN \
  apt-get update -y && \
  apt-get install -y -q pwgen postfix postfix-pcre dovecot-common dovecot-core dovecot-imapd opendkim opendkim-tools rsyslog supervisor vim procps

ADD dovecot/dovecot.conf /etc/dovecot/dovecot.conf
ADD opendkim/opendkim.conf /etc/opendkim.conf
ADD dovecot/dovecot /etc/init.d/dovecot
ADD postfix/master.cf /etc/postfix/master.cf
ADD postfix/transport /etc/postfix/transport
ADD container/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ADD container/init.sh /init.sh
ADD container/regenpasswd.sh /usr/local/bin/regenpasswd.sh
ADD container/regenpasswd.sh /usr/local/bin/removemail.sh
ADD container/pqueue /usr/local/bin/pqueue

RUN chmod +x /init.sh
RUN chmod +x /usr/local/bin/regenpasswd.sh
RUN chmod +x /usr/local/bin/removemail.sh
RUN chmod +x /usr/local/bin/pqueue

RUN sed -i 's/^mydestination = \$myhostname,/mydestination =/g' /etc/postfix/main.cf

CMD ["/usr/bin/supervisord"]
