FROM debian:stretch-slim
MAINTAINER 42wim

ENV DEBIAN_FRONTEND noninteractive
ENV VIRUSMAILS_DELETE_DELAY=7
ENV ONE_DIR=0
ENV ENABLE_POSTGREY=0
ENV FETCHMAIL_POLL=300
ENV POSTGREY_DELAY=300
ENV POSTGREY_MAX_AGE=35
ENV POSTGREY_TEXT="Delayed by postgrey"

ENV SASLAUTHD_MECHANISMS=pam
ENV SASLAUTHD_MECH_OPTIONS=""

# Packages
RUN apt-get update -q --fix-missing && \
  apt-get -y upgrade && \
  apt-get -y install postfix && \
  apt-get -y install --no-install-recommends \
    ca-certificates \
    curl \
    dovecot-core \
    dovecot-imapd \
    dovecot-ldap \
    dovecot-lmtpd \
    dovecot-managesieved \
    dovecot-pop3d \
    dovecot-sieve \
    ed \
    file \
    gnupg \
    iproute2 \
    locales \
    libmail-spf-perl \
    libnet-dns-perl \
    libsasl2-modules \
    netcat-openbsd \
    opendkim \
    opendkim-tools \
    opendmarc \
    postfix-ldap \
    postfix-pcre \
    postfix-policyd-spf-python \
    rsyslog \
    sasl2-bin \
    supervisor \
    postgrey \
    && \
  apt-get autoclean && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /usr/share/locale/* && \
  rm -rf /usr/share/man/* && \
  rm -rf /usr/share/doc/* && \
  touch /var/log/auth.log && \
  update-locale && \
  rm -f /etc/cron.weekly/fstrim

# Configures Dovecot
COPY target/dovecot/auth-passwdfile.inc target/dovecot/??-*.conf /etc/dovecot/conf.d/
RUN sed -i -e 's/include_try \/usr\/share\/dovecot\/protocols\.d/include_try \/etc\/dovecot\/protocols\.d/g' /etc/dovecot/dovecot.conf && \
  sed -i -e 's/#mail_plugins = \$mail_plugins/mail_plugins = \$mail_plugins sieve/g' /etc/dovecot/conf.d/15-lda.conf && \
  sed -i -e 's/^.*lda_mailbox_autocreate.*/lda_mailbox_autocreate = yes/g' /etc/dovecot/conf.d/15-lda.conf && \
  sed -i -e 's/^.*lda_mailbox_autosubscribe.*/lda_mailbox_autosubscribe = yes/g' /etc/dovecot/conf.d/15-lda.conf && \
  sed -i -e 's/^.*postmaster_address.*/postmaster_address = '${POSTMASTER_ADDRESS:="postmaster@domain.com"}'/g' /etc/dovecot/conf.d/15-lda.conf && \
  sed -i 's/#imap_idle_notify_interval = 2 mins/imap_idle_notify_interval = 29 mins/' /etc/dovecot/conf.d/20-imap.conf && \
  cd /usr/share/dovecot && \
  ./mkcert.sh  && \
  mkdir /usr/lib/dovecot/sieve-pipe && \
  chmod 755 /usr/lib/dovecot/sieve-pipe  && \
  mkdir /usr/lib/dovecot/sieve-filter && \
  chmod 755 /usr/lib/dovecot/sieve-filter

# Enables Postgrey
COPY target/postgrey/postgrey /etc/default/postgrey
COPY target/postgrey/postgrey.init /etc/init.d/postgrey
RUN chmod 755 /etc/init.d/postgrey && \
  mkdir /var/run/postgrey && \
  chown postgrey:postgrey /var/run/postgrey

# Configure DKIM (opendkim)
# DKIM config files
COPY target/opendkim/opendkim.conf /etc/opendkim.conf
COPY target/opendkim/default-opendkim /etc/default/opendkim

# Configure DMARC (opendmarc)
COPY target/opendmarc/opendmarc.conf /etc/opendmarc.conf
COPY target/opendmarc/default-opendmarc /etc/default/opendmarc
COPY target/opendmarc/ignore.hosts /etc/opendmarc/ignore.hosts

# Configures Postfix
COPY target/postfix/main.cf target/postfix/master.cf target/postfix/recipient_access.pcre /etc/postfix/
COPY target/postfix/sender_header_filter.pcre /etc/postfix/maps/sender_header_filter.pcre
RUN echo "" > /etc/aliases && \
  openssl dhparam -out /etc/postfix/dhparams.pem 2048

# no syslog user in debian compared to ubuntu
RUN adduser --system syslog && \
    useradd -u 5000 -d /home/docker -s /bin/bash -p $(echo docker | openssl passwd -1 -stdin) docker

# Configuring Logs
RUN mkdir -p /var/log/mail && \
  chown syslog:root /var/log/mail && \
  sed -i -r 's|/var/log/mail|/var/log/mail/mail|g' /etc/rsyslog.conf && \
  sed -i -r 's|;auth,authpriv.none|;mail.none;mail.error;auth,authpriv.none|g' /etc/rsyslog.conf && \
  # prevent syslog logrotate warnings \
  sed -i -e 's/\(printerror "could not determine current runlevel"\)/#\1/' /usr/sbin/invoke-rc.d && \
  sed -i -e 's/^\(POLICYHELPER=\).*/\1/' /usr/sbin/invoke-rc.d

# Get LetsEncrypt signed certificate
RUN curl -s https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.pem > /etc/ssl/certs/lets-encrypt-x3-cross-signed.pem

COPY ./target/bin /usr/local/bin
# Start-mailserver script
COPY ./target/check-for-changes.sh ./target/start-mailserver.sh ./target/postfix-wrapper.sh ./target/docker-configomat/configomat.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/*

# Configure supervisor
COPY target/supervisor/supervisord.conf /etc/supervisor/supervisord.conf
COPY target/supervisor/conf.d/* /etc/supervisor/conf.d/

EXPOSE 25 587 143 465 993 110 995 4190

CMD supervisord -c /etc/supervisor/supervisord.conf
