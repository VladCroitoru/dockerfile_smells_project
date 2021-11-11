From debian:jessie
MAINTAINER Timothée Eid <timothee.eid@erizo.fr>

# Set noninteractive mode for apt-get
ENV DEBIAN_FRONTEND noninteractive

# SMTP (Plain)
EXPOSE 25
# SMTP (StartSSL)
EXPOSE 587
# SMTP (SSL)
EXPOSE 465

VOLUME /var/spool/postfix
VOLUME /etc/ssl/localcerts
VOLUME /etc/postfix

# Install postfix
RUN apt-get update && apt-get install -y \
	openssl \
	rsyslog \
	postfix \
	postfix-ldap \
	opendkim \
	opendkim-tools \
	sasl2-bin \
	libsasl2-modules-ldap \
&& rm -rf /var/lib/apt/lists/*

# Enable auth daemon
RUN sed -i 's/^START=.*$/START=yes/' /etc/default/saslauthd
RUN sed -i 's/^MECHANISMS=.*$/MECHANISMS="ldap"/' /etc/default/saslauthd
RUN sed -i 's/^OPTIONS=.*$/OPTIONS="-c -m \/var\/spool\/postfix\/var\/run\/saslauthd"/' /etc/default/saslauthd
RUN adduser postfix sasl
RUN ln -s /etc/postfix/saslauthd.conf /etc/saslauthd.conf


# Add postfix conf
ADD resources /

# Setup startup script
ADD entrypoint.sh /entrypoint.sh
CMD ["/entrypoint.sh"]