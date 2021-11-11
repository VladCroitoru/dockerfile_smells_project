FROM debian:buster

ENV PATH="/container/scripts:${PATH}"
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -q -y update \
 && apt-get -q -y install --no-install-recommends runit \
                          openssl \
                          rsyslog \
                          net-tools \
                          procps \
                          \
                          mariadb-client \
                          mariadb-server \
                          \
                          dovecot-imapd \
                          dovecot-lmtpd \
                          dovecot-mysql \
                          dovecot-sieve dovecot-managesieved \
                          \
                          postfix \
                          postfix-mysql \
                          \
 && apt-get -q -y clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
 \
 && head -n $(grep -n RULES /etc/rsyslog.conf | cut -d':' -f1) /etc/rsyslog.conf > /etc/rsyslog.conf.new \
 && mv /etc/rsyslog.conf.new /etc/rsyslog.conf \
 && echo '*.*        /dev/stdout' >> /etc/rsyslog.conf \
 && sed -i '/imklog/d' /etc/rsyslog.conf \
 \
 && echo ">> add user" \
 && addgroup --gid 5000 vmail \
 && adduser --ingroup vmail --uid 5000 --home /var/vmail --shell /bin/false --disabled-password --gecos "" vmail \
 \
 && touch /etc/mtab \
 \
 && openssl dhparam -out /etc/postfix/dh1024.pem 1024 \
 && openssl dhparam -out /etc/postfix/dh512.pem 512

COPY config /etc/

# postfix
EXPOSE 25 465 587

# dovecot
EXPOSE 110 143 993 995 4190

VOLUME ["/etc/postfix/tls", "/etc/postfix/additional", "/var/vmail"]

COPY . /container/
HEALTHCHECK CMD ["/container/scripts/docker-healthcheck.sh"]
ENTRYPOINT ["entrypoint.sh"]
