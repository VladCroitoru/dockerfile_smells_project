FROM php:7.4

# setup the python environment
WORKDIR /tmp
RUN apt-get update && apt-get install -y wget git tar python unzip
RUN wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
RUN python get-pip.py
RUN pip install PyYaml
RUN pip install -U pytest
RUN pip install httplib2

# install php composer
RUN cd \
  && curl -sS https://getcomposer.org/installer | php \
  && ln -s /root/composer.phar /usr/local/bin/composer

# add source code and libs
ADD . /home

# setup tde libs
WORKDIR /home/libs
RUN tar xvzf TDE-API-Python-Linux-64Bit.gz
WORKDIR DataExtract-8300.15.0308.1149
RUN python setup.py build
RUN python setup.py install

#setup php app
WORKDIR /home/php
RUN composer install --no-interaction

WORKDIR /home
RUN du -sh *
CMD ./src/run.sh
