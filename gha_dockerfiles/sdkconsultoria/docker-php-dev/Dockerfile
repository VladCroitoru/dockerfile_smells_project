FROM ubuntu

ARG DEBIAN_FRONTEND=noninteractive

RUN  apt-get update && \
     apt-get -y install \
             software-properties-common

RUN apt-get install rsync grsync  -y
RUN apt-get install ssh  -y
RUN apt-get install webp  -y
RUN apt-get install mysql-client  -y
RUN apt-get install unzip  -y

# Install Apache and PHP
RUN add-apt-repository ppa:ondrej/php && \
    apt-get update && \
    apt-get -y install \
            zip \
            curl \
            apache2 \
            php8.0 \
            libapache2-mod-php8.0 \
            php8.0-mysql \
            php8.0-curl \
            php8.0-gd \
            php8.0-imagick \
            php8.0-cli \
            php8.0-mbstring \
            php8.0-zip \
            php8.0-xml \
            php8.0-soap \
            php8.0-xdebug \
            php8.0-pcov \
            php8.0-redis \
       --no-install-recommends && \
       apt-get clean && \
       rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Enable apache mods
RUN a2enmod rewrite headers expires php8.0

RUN curl -sS https://getcomposer.org/installer -o composer-setup.php && \
    php composer-setup.php --install-dir=/usr/local/bin --filename=composer && \
    composer clear-cache

# Install NodeJS
RUN apt -y install dirmngr apt-transport-https lsb-release ca-certificates

RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -

RUN apt -y install nodejs

# Install deployer
RUN curl -LO https://deployer.org/deployer.phar
RUN mv deployer.phar /usr/local/bin/dep
RUN chmod +x /usr/local/bin/dep

COPY image-files/ /

RUN rm ~/.ssh -rf
RUN mkdir ~/.ssh && ln -s /run/secrets/host_ssh_key ~/.ssh/id_rsa

WORKDIR /app

EXPOSE 80

ADD start.sh /
RUN chmod +x /start.sh

CMD ["/start.sh"]
#CMD ["/usr/sbin/apachectl","-DFOREGROUND"]
