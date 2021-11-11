########################################################################
# Dockerfile for a self-contained mail server
#
#                    ##        .
#              ## ## ##       ==
#           ## ## ## ##      ===
#       /""""""""""""""""\___/ ===
#  ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===- ~~~
#       \______ o          __/
#         \    \        __/
#          \____\______/
#
# Component:
# Author:       pjan vandaele <pjan@pjan.io>
# Scm url:      https://github.com/docxs/docker-mail
# License:      MIT
########################################################################

# pull base image
FROM docxs/base:latest

# maintainer details
MAINTAINER pjan vandaele "pjan@pjan.io"

# install packages
RUN \
  apt-prepare && \
  apt-get install -q -y \
    rsyslog \
    ssl-cert \
    postfix \
    postfix-pcre \
    libsasl2-modules \
    sasl2-bin \
    postgrey \
    dspam \
    dovecot-core \
    dovecot-imapd \
    dovecot-lmtpd \
    dovecot-sieve \
    dovecot-managesieved \
    dovecot-antispam &&\
  apt-cleanup

# Add configuration files
COPY ./config/etc_dovecot_conf.d_10-auth.conf    /etc/dovecot/conf.d/10-auth.conf
COPY ./config/etc_dovecot_conf.d_10-mail.conf    /etc/dovecot/conf.d/10-mail.conf
COPY ./config/etc_dovecot_conf.d_10-master.conf  /etc/dovecot/conf.d/10-master.conf
COPY ./config/etc_dovecot_conf.d_10-ssl.conf     /etc/dovecot/conf.d/10-ssl.conf
COPY ./config/etc_dovecot_conf.d_15-lda.conf     /etc/dovecot/conf.d/15-lda.conf
COPY ./config/etc_dovecot_conf.d_20-imap.conf    /etc/dovecot/conf.d/20-imap.conf
COPY ./config/etc_dovecot_conf.d_90-plugin.conf  /etc/dovecot/conf.d/90-plugin.conf
COPY ./config/etc_dovecot_dovecot.conf           /etc/dovecot/dovecot.conf
COPY ./config/etc_dspam_default.prefs            /etc/dspam/default.prefs
COPY ./config/etc_dspam_dspam.conf               /etc/dspam/dspam.conf
COPY ./config/etc_postfix_dspam_filter_access    /etc/postfix/dspam_filter_access
COPY ./config/etc_postfix_main.cf                /etc/postfix/main.cf
COPY ./config/etc_postfix_master.cf              /etc/postfix/master.cf
COPY ./config/etc_postfix_smtp_header_checks     /etc/postfix/smtp_header_checks

# Configure settings
VOLUME ["/settings"]

# vmail folder & user
VOLUME ["/data"]
RUN \
  groupadd -g 5000 vmail && \
  useradd -g vmail -u 5000 vmail -d /data -m

# Add the configure script
COPY ./bin/*  /bin/
RUN \
  chmod 755 /bin/mail-configure &&\
  chmod 755 /bin/mail-init &&\
  chmod 755 /bin/mail-run

# expose the relevant ports
EXPOSE \
  25 143 587 993

ENTRYPOINT \
  ["/bin/mail-run"]
