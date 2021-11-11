From debian:jessie
MAINTAINER Timothée Eid <timothee.eid@erizo.fr>

# Set noninteractive mode for apt-get
ENV DEBIAN_FRONTEND noninteractive

# IMAPs port
EXPOSE 993
# IMAP port
EXPOSE 143
# POPs port
EXPOSE 995
# POP port
EXPOSE 110
# LMTP port
EXPOSE 24

VOLUME /var/mail
VOLUME /etc/ssl/localcerts
VOLUME /etc/dovecot

# Install dovecot
RUN apt-get update && apt-get install -y \
	openssl \
	dovecot-imapd \
	dovecot-lmtpd \
	dovecot-ldap \
	dovecot-sieve \
	dovecot-managesieved \
&& rm -rf /var/lib/apt/lists/*

# Add default conf
ADD default_conf /etc/dovecot

# Setup startup script
ADD entrypoint.sh /entrypoint.sh
CMD ["/entrypoint.sh"]
