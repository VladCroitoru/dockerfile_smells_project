FROM pblaszczyk/debian-lenny

MAINTAINER Joeri Verdeyen <joeriv@yappa.be>

ENV DOCUMENT_ROOT /var/www/app/html
ENV ENVIRONMENT dev
ENV COMPOSER_ALLOW_SUPERUSER 1

RUN \
  apt-get update && \
  apt-get install -y \
    curl \
    wget \
    vim \
    git \
    locales \
    apache2 \
    php5 \
    php5-mysql \
    php5-mcrypt \
    php5-gd \
    php5-curl \
    php-pear \
    php-apc \
    php5-cli \
    php5-curl \
    php5-mcrypt \
    php5-sqlite \
    php5-tidy \
    php5-imap \
    php5-json \
    php5-imagick \
    libapache2-mod-php5 && \
  a2enmod proxy && \
  a2enmod proxy_http && \
  a2enmod alias && \
  a2enmod dir && \
  a2enmod env && \
  a2enmod mime && \
  a2enmod rewrite && \
  a2enmod status && \
  a2enmod filter && \
  a2enmod deflate && \
  a2enmod setenvif && \
  a2enmod vhost_alias && \
  apt-get autoremove -y && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists

RUN echo Europe/Brussels > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

RUN echo 'de_DE ISO-8859-1\n\
de_DE.UTF-8 UTF-8\n\
de_DE@euro ISO-8859-15\n\
en_GB ISO-8859-1\n\
en_GB.ISO-8859-15 ISO-8859-15\n\
en_US ISO-8859-1\n\
en_US.ISO-8859-15 ISO-8859-15\n\
en_US.UTF-8 UTF-8\n\
fr_FR ISO-8859-1\n\
fr_FR.UTF-8 UTF-8\n\
fr_FR@euro ISO-8859-15\n\
nl_BE ISO-8859-1\n\
nl_BE.UTF-8 UTF-8\n\
nl_BE@euro ISO-8859-15\n\
nl_NL ISO-8859-1\n\
nl_NL.UTF-8 UTF-8\n\
nl_NL@euro ISO-8859-15\n'\
>> /etc/locale.gen &&  \
usr/sbin/locale-gen

RUN ln -sf /dev/stderr /var/log/apache2/error.log

#ADD htpasswd.conf /etc/apache2/conf-available/htpasswd.conf

COPY dummy.crt  /etc/ssl/crt/dummy.crt
COPY dummy.key  /etc/ssl/crt/dummy.key
COPY default.conf /etc/apache2/sites-available/default
COPY php.ini    /etc/php5/apache2/conf.d/
COPY php.ini    /etc/php5/cli/conf.d/
COPY run.sh /run.sh

RUN chmod +x run.sh

EXPOSE 80 433

ENTRYPOINT ["/bin/bash", "/run.sh"]