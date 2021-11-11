FROM ubuntu:14.04
MAINTAINER Johannes Steu <js@johannessteu.de>

USER root

# Install dependecies
RUN apt-get update -y && apt-get install -y git-core nginx curl nano git php5-fpm php5-cli php5-mysql php5-intl php5-mcrypt php5-apcu php5-gd php5-curl php5-sqlite graphicsmagick mysql-client mysql-server php5-ldap
RUN curl -s https://getcomposer.org/installer | php &&  mv composer.phar /usr/local/bin/composer

# add files
ADD docker-files /

RUN mkdir -p /var/www

# install typo3
RUN cd /var/www && git clone http://git.typo3.org/Packages/TYPO3.CMS.git

RUN cp -R /var/www/TYPO3.CMS /var/www/typo3_7-6

RUN cd /var/www/typo3_7-6 && git checkout TYPO3_7-6
RUN cd /var/www/typo3_7-6 && sed -i s/"\"authors\""/"\"repositories\": [{\"type\": \"composer\", \"url\": \"https:\/\/composer.typo3.org\"},{ \"type\": \"git\", \"url\": \"https:\/\/github.com\/helhum\/typo3_console.git\" }],\"authors\""/g composer.json
RUN cd /var/www/typo3_7-6 && composer update
RUN mkdir -p /var/www/typo3_7-6/typo3conf/ext
RUN cd /var/www/typo3_7-6/typo3conf/ext && git clone https://github.com/TYPO3-Console/typo3_console.git
#RUN cd /var/www/typo3_7-6 && cat composer.json
#RUN cd /var/www/typo3_7-6 && composer require helhum/typo3-console 1.2.5
#RUN cd /var/www/typo3_7-6 && composer update --ignore-platform-reqs