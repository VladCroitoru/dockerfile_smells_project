FROM php:7.2-fpm

RUN echo 'date.timezone = "Europe/Vienna"' > /usr/local/etc/php/conf.d/timezone.ini

ENV VERSION 8.1.7
ENV NVM_VERSION 0.33.8
ENV NODE_VERSION 8.11.1
ENV NVM_DIR /usr/local/nvm
ENV PATH /usr/local/nvm/versions/node/v$NODE_VERSION/bin:$PATH

RUN apt-get update && \
  apt-get -y install --no-install-recommends git zlib1g-dev unzip && \
  apt-get clean && rm -rf /var/lib/apt/lists/*
RUN docker-php-ext-install -j$(nproc) zip

RUN curl -sSfL -o- https://raw.githubusercontent.com/creationix/nvm/v${NVM_VERSION}/install.sh | bash
RUN npm install --global gulp-cli

RUN chown www-data ../ -R
USER www-data

RUN curl -sSfL -o - https://github.com/afterlogic/webmail-pro-8/archive/${VERSION}.tar.gz | tar xz --strip-components 1
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
  php -r "if (hash_file('SHA384', 'composer-setup.php') === '544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" && \
  php composer-setup.php && \
  php -r "unlink('composer-setup.php');"
RUN php composer.phar install
RUN npm install ./modules/CoreWebclient
RUN gulp styles --themes Default,DeepForest,Funny
RUN gulp js:min
