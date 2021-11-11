FROM dougbtv/asterisk
MAINTAINER Dmitry Romanov "dmitry.romanov85@gmail.com"
USER root

RUN ["yum", "install", "-y", "sudo", "wget", "mc"]
RUN ["wget", "http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-9.noarch.rpm"]
RUN ["wget", "http://rpms.famillecollet.com/enterprise/remi-release-7.rpm"]
RUN ["rpm", "-Uvh", "remi-release-7*.rpm", "epel-release-7*.rpm"]
RUN ["yum", "install", "--enablerepo=remi-php71", "-y", "php-cli", "php-pgsql", "php-xml", "php-mbstring", "php-pecl-zip"]
RUN curl -s https://getcomposer.org/installer | php
RUN ["mv", "composer.phar", "/usr/local/bin/composer"]
RUN sed -i "s/;date.timezone =.*/date.timezone = Europe\/Moscow/" /etc/php.ini

RUN wget -O /usr/lib64/asterisk/modules/codec_g729.so http://asterisk.hosting.lv/bin/codec_g729-ast110-gcc4-glibc-x86_64-pentium4.so

RUN wget --no-check-certificate http://sourceforge.net/projects/lame/files/lame/3.99/lame-3.99.tar.gz && \
  tar zxvf lame-3.99.tar.gz && \
  cd lame-3.99 && \
  ./configure && \
  make && \
  make install
