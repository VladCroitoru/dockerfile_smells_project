FROM phusion/baseimage
MAINTAINER Mario Fahlandt <dasyoshi@gmail.com>


# ensure UTF-8
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# change resolv.conf
#RUN echo 'nameserver 8.8.8.8' > /etc/resolv.conf

# setup
ENV HOME /root
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

CMD ["/sbin/my_init"]

# nginx-php installation
RUN DEBIAN_FRONTEND="noninteractive" add-apt-repository ppa:ondrej/php
RUN DEBIAN_FRONTEND="noninteractive" apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y upgrade
RUN DEBIAN_FRONTEND="noninteractive" apt-get update --fix-missing
RUN DEBIAN_FRONTEND="noninteractive" apt-cache policy search php7.1*
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install php7.1
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install php7.1-fpm php7.1-common php7.1-cli php7.1-mysqlnd php7.1-mcrypt php7.1-curl php7.1-bcmath php7.1-mbstring php7.1-soap php7.1-xml php7.1-zip php7.1-json php7.1-imap php-xdebug php-pgsql

# install nginx (full)
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y nginx-full

# install git
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y git

# install apache2 utils to enable htpassd
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y apache2-utils
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y curl
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y build-essential

# install nodeJS


# gpg keys listed at https://github.com/nodejs/node#release-team
RUN set -ex \
  && for key in \
    9554F04D7259F04124DE6B476D5A82AC7E37093B \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
    B9AE9905FFD7803F25714661B63B535A4C206CA9 \
    C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
    56730D5401028683275BD23C23EFEFE93C4CFFFE \
  ; do \
    gpg --keyserver pgp.mit.edu --recv-keys "$key" || \
    gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \
  done

ENV NPM_CONFIG_LOGLEVEL info
ENV NODE_VERSION 6.10.3

RUN buildDeps='xz-utils curl ca-certificates' \
    && set -x \
    && apt-get update && apt-get install -y $buildDeps --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
    && curl -SLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
    && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
    && grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
    && tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
    && rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt \
    && ln -s /usr/local/bin/node /usr/local/bin/nodejs


# install php composer
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer
RUN composer global require hirak/prestissimo

# add build script (also set timezone to Americas/Sao_Paulo)
RUN mkdir -p /root/setup
ADD build/setup.sh /root/setup/setup.sh
RUN chmod +x /root/setup/setup.sh
RUN (cd /root/setup/; /root/setup/setup.sh)

# copy files from repo
ADD build/nginx.conf /etc/nginx/sites-available/default
ADD build/.bashrc /root/.bashrc

# disable services start
RUN update-rc.d -f apache2 remove
RUN update-rc.d -f nginx remove
RUN update-rc.d -f php7.1-fpm remove

# add startup scripts for nginx
ADD build/nginx.sh /etc/service/nginx/run
RUN chmod +x /etc/service/nginx/run

# add startup scripts for php7.1-fpm
ADD build/phpfpm.sh /etc/service/phpfpm/run
RUN chmod +x /etc/service/phpfpm/run

# set WWW public folder
RUN mkdir -p /var/www/public
ADD build/index.php /var/www/public/index.php

RUN chown -R www-data:www-data /var/www
RUN chmod 755 /var/www

# set terminal environment
ENV TERM=xterm

# port and settings
EXPOSE 80 443 9000

# cleanup apt and lists
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get clean
RUN apt-get autoclean