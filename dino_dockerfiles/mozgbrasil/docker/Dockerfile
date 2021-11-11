FROM php:7.0-apache

LABEL Marcio dos Santos Amorim <suporte@mozg.com.br>

ENV XDEBUG_PORT 9000

# Fix debconf warnings upon build
ARG DEBIAN_FRONTEND=noninteractive

## Install System Dependencies

RUN pwd && ls -lah && apt-get update && apt-get install -y --no-install-recommends software-properties-common  libfreetype6-dev libicu-dev libssl-dev libjpeg62-turbo-dev libmcrypt-dev libedit-dev libedit2 libxslt1-dev redis-tools mysql-client vim apt-utils wget git nano curl lynx psmisc p7zip-full unzip tar cron bash-completion dialog openssh-server

# E: Package 'python-software-properties' has no installation candidate
# python-software-properties libpng12-dev

## Install Webserver Dependencies

RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/

RUN docker-php-ext-install opcache gd bcmath intl mbstring mcrypt pdo_mysql soap xsl zip sockets calendar

## Install Composer

#COPY --from=composer:1.6 /usr/bin/composer /usr/bin/composer

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin/ --filename=composer && composer --version

#RUN ls -lah $HOME

#RUN composer global require hirak/prestissimo

## Install oAuth

#RUN apt-get install -y libpcre3 libpcre3-dev && pecl install oauth && echo "extension=oauth.so" > /usr/local/etc/php/conf.d/docker-php-ext-oauth.ini

## Install Mhsendmail

RUN DEBIAN_FRONTEND=noninteractive apt-get -y install golang-go && mkdir /opt/go && export GOPATH=/opt/go && go get github.com/mailhog/mhsendmail

## Install Node, NVM, NPM and Grunt

#RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && apt-get install -y nodejs build-essential && curl https://raw.githubusercontent.com/creationix/nvm/v0.16.1/install.sh | sh && npm i -g grunt-cli yarn

## Install XDebug

#RUN yes | pecl install xdebug && echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.iniOLD 

## Install n98magerun

#RUN wget https://files.magerun.net/n98-magerun.phar && chmod +x ./n98-magerun.phar && mv ./n98-magerun.phar /usr/local/bin/

## Install n98magerun2

#RUN wget https://files.magerun.net/n98-magerun2.phar && chmod +x ./n98-magerun2.phar && mv ./n98-magerun2.phar /usr/local/bin/

## Install m2install

#RUN curl -o /etc/bash_completion.d/m2install-bash-completion https://raw.githubusercontent.com/yvoronoy/m2install/master/m2install-bash-completion

## Install n98magerun2 autocompletion

#RUN curl -o /etc/bash_completion.d/n98-magerun2.phar.bash https://raw.githubusercontent.com/netz98/n98-magerun2/master/res/autocompletion/bash/n98-magerun2.phar.bash

#RUN echo "source /etc/bash_completion" >> /root/.bashrc
#RUN echo "source /etc/bash_completion" >> /var/www/.bashrc

## Install ioncube loader

#RUN curl -fsSL 'http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz' -o ioncube.tar.gz && mkdir -p ioncube && tar -xf ioncube.tar.gz -C ioncube --strip-components=1 && rm ioncube.tar.gz && mv ioncube/ioncube_loader_lin_7.0.so /var/www/ioncube_loader_lin_7.0.so && rm -r ioncube 

##


## Configuring system

#ADD .docker/config/php.ini /usr/local/etc/php/php.ini
#ADD .docker/config/magento.conf /etc/apache2/sites-available/magento.conf
#ADD .docker/config/custom-xdebug.ini /usr/local/etc/php/conf.d/custom-xdebug.ini
#COPY .docker/bin/* /usr/local/bin/
#COPY .docker/users/* /var/www/
#RUN chmod +x /usr/local/bin/*
#RUN ln -s /etc/apache2/sites-available/magento.conf /etc/apache2/sites-enabled/magento.conf

COPY ./php-conf/ /usr/local/etc/php/conf.d/
COPY ./php-conf/disabled/ /usr/local/etc/php/conf.d/

#COPY ./apache-conf/docker-library/ /etc/apache2/sites-available/

RUN a2enmod proxy_fcgi setenvif actions rewrite headers

RUN chmod 777 -Rf /var/www /var/www/.* && chown -Rf www-data:www-data /var/www /var/www/.* && usermod -u 1000 www-data && chsh -s /bin/bash www-data

VOLUME /var/www/html
WORKDIR /var/www/html