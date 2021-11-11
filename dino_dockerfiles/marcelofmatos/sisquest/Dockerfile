# A basic config. for phpnetmap

FROM tutum/apache-php

MAINTAINER Marcelo Matos <marcelo.matos@ufrr.br>

RUN apt-get update \
    && apt-get install -y php5-mysql git apache2-utils cabextract xfonts-utils wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && wget http://ftp.us.debian.org/debian/pool/contrib/m/msttcorefonts/ttf-mscorefonts-installer_3.6_all.deb \
    && dpkg -i ttf-mscorefonts-installer_3.6_all.deb \
    && rm ttf-mscorefonts-installer_3.6_all.deb

# code
RUN rm -rf /app && cd / && git clone https://github.com/marcelofmatos/sisquest.git app

# container config
ENV ALLOW_OVERRIDE true
RUN a2enmod rewrite authz_groupfile \
    && echo 'error_reporting = E_ALL & ~E_DEPRECATED & ~E_STRICT & ~E_NOTICE' > /etc/php5/mods-available/custom.ini \
    && echo 'short_open_tag = on' >> /etc/php5/mods-available/custom.ini \
    && echo 'disable_functions = ' >> /etc/php5/mods-available/custom.ini \
    && echo 'AddDefaultCharset UTF-8' > /etc/apache2/conf-available/charset.conf \
    && php5enmod custom \
    && sed -i '2i /app/set_htpasswd.sh' /run.sh \
    && chmod +x /app/set_htpasswd.sh 
