FROM ubuntu:xenial

MAINTAINER furiousgeorge <furiousgeorgecode@gmail.com>

ENV INSTALL_LIST apache2 php7.0 libapache2-mod-php7.0 php7.0-mysql php7.0-curl php7.0-gd php7.0-intl ffmpeg libimage-exiftool-perl python git curl python-pip

RUN apt-get update \
    && apt-get install -qy $INSTALL_LIST \
    && rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/* /root/.cache \
    && a2enmod rewrite

WORKDIR /var/www/html

RUN cd /var/www/html \
    && rm -f index.html \
    && git clone https://github.com/DanielnetoDotCom/YouPHPTube-Encoder . \
    && pip install --upgrade pip \
    && pip install youtube-dl

ADD 000-default.conf /etc/apache2/sites-enabled/000-default.conf

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
