FROM php:5.4-cli

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN apt-get update && \
    apt-get install wget git python-pip jq gettext-base openssl zip build-essential libssl-dev -y

RUN docker-php-ext-install mbstring pcntl

RUN curl -s https://getcomposer.org/installer --output composer-setup.php && \
    php composer-setup.php --filename=composer --install-dir=/usr/local/bin && \
    chmod a+rx /usr/local/bin/composer

RUN wget http://rocketeer.autopergamene.eu/versions/rocketeer.phar && \
    chmod +x rocketeer.phar && \
    mv rocketeer.phar /usr/local/bin/rocketeer

RUN pip install awscli

# INstalling Node.js and NVM/NPM

ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 8.9.3

RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.31.0/install.sh | bash && \
    . $NVM_DIR/nvm.sh && \
    nvm install $NODE_VERSION

ENV NODE_PATH $NVM_DIR/versions/node/v$NODE_VERSION/lib/node_modules
ENV PATH      $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH