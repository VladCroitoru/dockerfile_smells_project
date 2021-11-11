# A custom data container with SSHd service
#

FROM php
MAINTAINER Jingsheng Wang <jingsheng.wang@insready.com>

RUN apt-get update && apt-get install -y openssh-server git nano libpng12-dev libjpeg-dev libpq-dev mariadb-client \
	&& rm -rf /var/lib/apt/lists/* \
	&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
	&& docker-php-ext-install gd mbstring pdo pdo_mysql pdo_pgsql zip bcmath

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

RUN mkdir /var/run/sshd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
ENV TERM xterm

RUN echo "export VISIBLE=now" >> /etc/profile

WORKDIR /var/www/html

# The custom entrypoint is used to link all host read-only files
RUN mkdir /data
COPY docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 22

ENTRYPOINT ["/entrypoint.sh"]
