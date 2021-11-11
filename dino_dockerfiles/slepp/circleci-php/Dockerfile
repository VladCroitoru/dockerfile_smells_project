FROM circleci/php:7.1

RUN sudo apt-get update \
    && sudo apt-get install -y \
      libssl-dev \
      zlib1g-dev \
    && sudo apt-get clean \
    && sudo rm -rf /var/lib/apt/lists/*

RUN sudo pecl install mongodb \
    && echo 'extension=mongodb.so' | sudo tee /usr/local/etc/php/conf.d/mongodb.ini

RUN sudo docker-php-ext-install zip
