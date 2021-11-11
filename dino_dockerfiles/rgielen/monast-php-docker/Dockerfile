FROM ubuntu:trusty
MAINTAINER "Rene Gielen" <rgielen@apache.org>

RUN apt-get update && apt-get upgrade -y \
      && apt-get install -y --no-install-recommends \
           apache2 \
           php5 \
           php5-cli \
           expect \
           libapache2-mod-php5 \
           wget \
           unzip \
           gettext-base \
           ca-certificates \
      && apt-get clean \
      && rm -rf /var/lib/apt/lists/* \
      && rm -rf /tmp/*

ADD install-pear.sh /
RUN wget -O /tmp/go-pear.phar http://pear.php.net/go-pear.phar && /install-pear.sh && pear install HTTP_Client && rm /install-pear.sh

RUN wget https://github.com/dagmoller/monast/archive/master.zip \
        && unzip master.zip \
        && rm -rf monast-master/pymon \
        && mv monast-master /monast-php \
        && chgrp -R www-data /monast-php \
        && rm master.zip

ADD 000-default.conf /etc/apache2/sites-available/
ADD config-template.php /
ADD configure-and-start.sh /

ENV PYMON_HOST=localhost
ENV PYMON_PORT=5039
ENV MONAST_LANGUAGE=en

EXPOSE 80
ENTRYPOINT ["/configure-and-start.sh", "-D", "FOREGROUND"]
