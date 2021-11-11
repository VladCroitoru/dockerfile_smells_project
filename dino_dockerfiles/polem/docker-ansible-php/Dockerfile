FROM williamyeh/ansible:ubuntu16.04

RUN apt-get update
RUN apt-get -y install unzip php php-zip git

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
  && php composer-setup.php --install-dir=bin --filename=composer \
  && php -r "unlink('composer-setup.php');"
