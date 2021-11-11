FROM eboost/php7fpm

MAINTAINER Bert van Hoekelen <bert@eboost.co>

RUN apt-get update \
    && apt-get install -y \
        fontconfig \
        xfonts-75dpi \
        libxrender1 \
        xfonts-base \
        libjpeg62-turbo \
        libxext6 \
        git \
        wget \
        supervisor \
    && wget -O wkhtmltox.deb http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-jessie-amd64.deb \
    && dpkg -i wkhtmltox.deb

CMD ["/usr/bin/supervisord"]
