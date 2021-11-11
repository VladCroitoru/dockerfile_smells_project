FROM php:7.0-cli

WORKDIR /app

ADD . /app


RUN apt-get update 
RUN apt-get -y install git unzip net-tools
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php -r "if (hash_file('SHA384', 'composer-setup.php') === '669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
RUN php composer-setup.php
RUN php -r "unlink('composer-setup.php');"

RUN php ./composer.phar --no-plugins --no-scripts install

EXPOSE 80

ENV TM_DATA data.data
ENV TM_PORT 80

CMD ["php", "server.php"]

