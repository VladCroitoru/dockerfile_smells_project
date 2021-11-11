FROM debian:stable
MAINTAINER mildred

RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y daemontools
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y dovecot-core dovecot-imapd dovecot-lmtpd dovecot-managesieved dovecot-sieve
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y exim4 exim4-daemon-heavy
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y daemontools-run

# Debug
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y net-tools netcat procps man nano lsof less

VOLUME /var/mail
VOLUME /var/log/exim
VOLUME /var/log/dovecot
VOLUME /var/spool/exim4
WORKDIR /

RUN { \
  ln -s /var/mail/users /etc/dovecot/users; \
  echo "/etc/exim/exim.conf" >> /etc/exim4/trusted_configs; \
  groupadd ssl; \
  useradd vmail; \
  usermod -a -G ssl Debian-exim; \
  usermod -a -G ssl dovecot; \
  }

COPY dovecot.service            /etc/service/dovecot
COPY exim.service               /etc/service/exim
COPY mark-submission-read.sieve /etc/dovecot/mark-submission-read.sieve
COPY dovecot-local.conf         /etc/dovecot/local.conf
COPY exim.conf                  /etc/exim/exim.conf.src
COPY entry.sh                   /entry.sh

# sieve=4190 imaps=993 imap2=143 smtp=25 smtps=465 submission=587
EXPOSE 4190 993 143 25 465 587

ENTRYPOINT ["/bin/bash", "/entry.sh"]
CMD ["init"]

