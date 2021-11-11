FROM debian:jessie

ENV FUSIONDIRECTORY_DEB_PKG_VERSION=1.0.9.3-1 \
    LDAP_DOMAIN=fovea.cc \
    LDAP_PASSWORD=changeme \
    FUSIONDIRECTORY_PASSWORD=changeme2 \
    SMTP_HOST=smtp \
    SMTP_PORT=25 \
    SMTP_TLSCERTCHECK=off

EXPOSE 80

RUN export DEBIAN_FRONTEND=noninteractive && \
    export LC_ALL=en_US.UTF-8 && \
    apt-get update && \
    apt-get install -y software-properties-common gnupg && \
    gpg --keyserver keys.gnupg.net --recv-keys E184859262B4981F && \
    gpg -a --export E184859262B4981F | apt-key add - && \
    add-apt-repository 'deb http://repos.fusiondirectory.org/fusiondirectory-releases/fusiondirectory-1.0.9/debian-jessie/ jessie main' && \
    apt-get update && \
    apt-get install -y php-mdb2 msmtp \
        fusiondirectory=${FUSIONDIRECTORY_DEB_PKG_VERSION} \
        fusiondirectory-plugin-mail=${FUSIONDIRECTORY_DEB_PKG_VERSION} && \
    rm -rf /var/lib/apt/lists/*

COPY apache.conf /etc/apache2/sites-available/000-default.conf
COPY fusiondirectory.conf /fusiondirectory.conf
COPY msmtp.conf /msmtp.conf
COPY start.sh /start.sh

ENTRYPOINT ["/start.sh"]
