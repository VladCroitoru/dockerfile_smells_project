FROM debian:jessie
MAINTAINER Ruzhentsev Alexandr noc@mirafox.ru

ADD https://github.com/validator/validator/releases/download/17.9.0/vnu.jar_17.9.0.zip /opt
ADD https://github.com/w3c/markup-validator/archive/master.zip /opt/markup-validator-master.zip

RUN echo deb http://httpredir.debian.org/debian jessie-backports main | tee /etc/apt/sources.list.d/backports.list \
    && apt-get update \
    && apt-get -y upgrade \
    && apt-get install -t jessie-backports -y \
        openjdk-8-jre-headless \
        ca-certificates-java \
    && apt-get install -y \
        apache2 \
        libapache2-mod-perl2 \
        openjdk-8-jdk \
        python \
        unzip \
        supervisor \
        opensp \
        libconfig-general-perl \
        libencode-hanextra-perl \
        libhtml-encoding-perl \
        libhtml-template-perl \
        libjson-perl \
        libsgml-parser-opensp-perl \
        libxml-libxml-perl \
        libnet-ip-perl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean \
    && mkdir -p /usr/local/validator \
    && mkdir -p /etc/w3c \
    && unzip -j /opt/vnu*.zip -d /opt/validator.nu \
    && unzip /opt/markup-validator-master.zip -d /opt \
    && rm -f /opt/*.zip \
    && mv /opt/markup-validator-master/htdocs /usr/local/validator \
    && mv /opt/markup-validator-master/share /usr/local/validator \
    && mv /opt/markup-validator-master/httpd/cgi-bin /usr/local/validator \
    && cp /usr/local/validator/htdocs/config/* /etc/w3c

COPY config/supervisord.conf /etc/supervisord.conf
COPY config/validator.conf /etc/w3c/validator.conf
COPY config/w3c-validator.conf /etc/apache2/conf-available/w3c-validator.conf
COPY scripts/docker-entrypoint.sh /usr/local/bin/

RUN a2enmod cgid expires include rewrite \
    && a2dismod perl \
    && a2enconf w3c-validator \
    && chmod 755 /usr/local/bin/docker-entrypoint.sh

WORKDIR /opt

EXPOSE 80 8888

CMD ["/usr/local/bin/docker-entrypoint.sh"]
