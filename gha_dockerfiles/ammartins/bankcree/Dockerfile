FROM ubuntu

ADD app /srv/app
ADD composer.json /srv/composer.json
ADD composer.lock /srv/composer.lock
ADD renovate.json /srv/renovate.json
ADD src /srv/src
ADD web /srv/web

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install sudo -y && \
    apt-get autoremove -y && \
    apt-get autoclean -y

ARG DEBIAN_FRONTEND=noninteractive

# Install PHP
RUN apt-get install software-properties-common -y && \
    add-apt-repository ppa:ondrej/php && \
    apt-get update && \
    apt-get install php7.3 php7.3-cli php7.3-xml php7.3-curl curl git libmysqlclient-dev zip unzip php-zip php7.3-mysql -y

# Install Composer
RUN curl -s https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer

WORKDIR /srv/

RUN composer install
#RUN php app/console assetic:dump --env=prod

ENTRYPOINT php app/console match:payments -- all
