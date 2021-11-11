FROM ubuntu:16.04

MAINTAINER Andrey F. Kupreychik <foxel@quickfox.ru>

ENV DEBIAN_FRONTEND=noninteractive

RUN \
    apt-get update && \
    apt-get -y --no-install-recommends install \
        wget supervisor rsyslog cron \
        postfix postfix-mysql \
        dovecot-core dovecot-imapd dovecot-lmtpd dovecot-mysql dovecot-sieve \
        libmail-dkim-perl libnet-ident-perl pyzor razor spamassassin spamc \
        default-jre-headless && \
    update-locale LANG=C.UTF-8 && \
    rm -rf /etc/logrotate.d/* && \
    rm -rf /var/lib/apt/lists/*

# Liquibase JARs
RUN \
    LIQUIBASE_VERSION=3.5.3 && \
    CONNECTOR_VERSION=5.1.34 && \
    CONNECTOR_NAME="mysql-connector-java-${CONNECTOR_VERSION}" && \
    CONNECTOR_FILENAME="${CONNECTOR_NAME}-bin.jar" && \
    mkdir -p /opt/liquibase && \
    wget -O- \
        "https://github.com/liquibase/liquibase/releases/download/liquibase-parent-${LIQUIBASE_VERSION}/liquibase-${LIQUIBASE_VERSION}-bin.tar.gz" | \
        tar -xz -C /opt/liquibase liquibase liquibase.jar && \
    wget -O- \
        "http://dev.mysql.com/get/Downloads/Connector-J/${CONNECTOR_NAME}.tar.gz" | \
        tar -xOz "${CONNECTOR_NAME}/${CONNECTOR_FILENAME}" > "/opt/liquibase/mysql-connector.jar" && \
    ln -s /opt/liquibase/liquibase /bin/liquibase

# Config defaults
# can be overwrited on start
ENV \
    DB_USERNAME=simpleone \
    DB_PASSWORD=simpleone \
    DB_NAME=simpleone \
    DB_HOSTNAME=mysql \
    DB_PREFIX=qfso_ \
    MAIL_HOSTNAME=example.com \
    MAIL_PROCESS_LIMIT=10 \
    MAIL_SSL_CERT_FILE="/etc/ssl/certs/ssl-cert-snakeoil.pem" \
    MAIL_SSL_KEY_FILE="/etc/ssl/private/ssl-cert-snakeoil.key"

COPY mailserver/ /opt/mailserver/
COPY etc/ /etc/

RUN \
    chmod +x /etc/scripts/*.sh && \
    groupadd -g 5000 vmail  && \
    useradd -g vmail -u 5000 vmail -d /var/mail && \
    # spamd
    mkdir -p /etc/spamassassin/sa-update-keys && \
    chmod 700 /etc/spamassassin/sa-update-keys && \
    echo "pyzor_options --homedir /var/lib/spamassassin/.pyzor" >> /etc/spamassassin/local.cf && \
    chown -R debian-spamd:debian-spamd /etc/spamassassin/sa-update-keys && \
    sed -i 's/^logfile = .*$/logfile = \/dev\/stderr/g' /etc/razor/razor-agent.conf

# SMTP submission(STARTTLS) IMAPS POP3S
EXPOSE 25 587 993 995

VOLUME ["/var/mail", "/var/log", "/var/lib/spamassassin"]

ENTRYPOINT ["/etc/scripts/startup.sh"]
