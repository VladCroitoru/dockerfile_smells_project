FROM ubuntu:14.04.2
ENV LC_ALL C
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

MAINTAINER Michell Campos <michellcampos13@gmail.com>
RUN apt-get -y update
RUN apt-get install -y -q software-properties-common wget
RUN add-apt-repository -y ppa:mozillateam/firefox-next
RUN add-apt-repository -y ppa:chris-lea/node.js
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list
RUN apt-get update -y
RUN apt-get install -y -q \
  firefox \
  google-chrome-beta \
  openjdk-7-jre-headless \
  nodejs \
  x11vnc \
  xvfb \
  xfonts-100dpi \
  xfonts-75dpi \
  xfonts-scalable \
  xfonts-cyrillic
RUN useradd -d /home/seleuser -m seleuser
RUN mkdir -p /home/seleuser/chrome
RUN chown -R seleuser /home/seleuser
RUN chgrp -R seleuser /home/seleuser
# fix https://code.google.com/p/chromium/issues/detail?id=318548
RUN mkdir -p /usr/share/desktop-directories
ADD ./bin/ /home/root/bin
RUN npm install -g \
  selenium-standalone@3.0.2 \
  phantomjs@1.9.12 && \
  selenium-standalone install

#INSTALL VIM
RUN apt-get update -qqy
RUN apt-get install vim -qqy

#INSTALL PHP
RUN apt-get install python-software-properties -y
RUN add-apt-repository ppa:ondrej/php5-5.6 -y
RUN apt-get update -qqy
RUN apt-get install curl php5 php5-xdebug php5-cli php5-curl git -y --force-yes

#INSTALL PHPUNIT
RUN apt-get update -qqy
RUN apt-get install wget -qqy
RUN wget https://phar.phpunit.de/phpunit.phar
RUN chmod +x phpunit.phar
RUN mv phpunit.phar /usr/local/bin/phpunit

#INSTALL COMPOSER
RUN apt-get update -qqy
RUN curl -sS https://getcomposer.org/installer | sudo php -- --install-dir=/usr/local/bin --filename=composer

EXPOSE 4444 5999
ENTRYPOINT ["sh", "/home/root/bin/start.sh"]
