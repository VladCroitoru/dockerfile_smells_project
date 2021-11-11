# Version dev-master 1.3.0
FROM php:5.5
MAINTAINER Berti Golf <info@berti-golf.de>
RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y git
WORKDIR /www
RUN bash -c "wget http://getcomposer.org/composer.phar && mv composer.phar /usr/local/bin/composer"
RUN  chmod a+x /usr/local/bin/composer
RUN  composer create-project --no-dev typo3/neos-base-distribution:dev-master TYPO3-Neos -n
WORKDIR /www/TYPO3-Neos/
VOLUME /www/TYPO3-Neos/
ADD php.ini  /usr/local/lib/php.ini
COPY docker-php-ext-* /usr/local/bin/
RUN chmod a+x  /usr/local/bin/docker-php-ext-*
RUN ls -la /usr/local/bin/*
RUN docker-php-ext-install mbstring
ENTRYPOINT ["/bin/bash"] 