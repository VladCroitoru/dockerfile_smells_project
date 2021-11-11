FROM ubuntu

# File Author / Maintainer
MAINTAINER brigzzy

ADD ./html /var/www/html
ADD ./esScripts /esScripts

# Update the repository sources list
RUN apt -yqq update

# Install and run apache
RUN apt -yqq install npm python-pip python-dev build-essential unzip git curl apache2 php libapache2-mod-php php-mcrypt php-curl && apt-get clean
RUN apt -yqq install vim telnet

WORKDIR /var/www/html
RUN npm i elasticsearch-csv
RUN easy_install pip
RUN pip install --upgrade pip
RUN pip install csv2es
RUN curl -s http://getcomposer.org/installer | php
RUN php composer.phar install --no-dev

WORKDIR /esScripts
RUN ./wait-for-it.sh -h elasticsearch -p 9200
RUN dbRestore.sh

EXPOSE 80
CMD apachectl -D FOREGROUND
# CMD /bin/bash
