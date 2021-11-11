FROM debian:jessie


MAINTAINER William Durand <william.durand1@gmail.com>


ENV DEBIAN_FRONTEND noninteractive
ENV DOCKER_COMPOSE_VERSION 1.4.1


RUN apt-get --quiet update

RUN apt-get install --yes --no-install-recommends wget git curl ca-certificates

# Node.js (and NPM).
RUN curl -sL https://deb.nodesource.com/setup | bash - \
    && apt-get install --yes nodejs \
    && curl -L https://www.npmjs.com/install.sh | sh

# HHVM.
RUN wget -q -O - http://dl.hhvm.com/conf/hhvm.gpg.key | apt-key add - \
    && echo deb http://dl.hhvm.com/debian jessie main | tee /etc/apt/sources.list.d/hhvm.list \
    && apt-get --quiet update \
    && apt-get install --yes hhvm

# Configure HHVM.
ADD etc/hhvm/php.ini /etc/hhvm/php.ini
RUN /usr/bin/update-alternatives --install /usr/bin/php php /usr/bin/hhvm 60

# Bundler.
RUN apt-get install --yes bundler

# Rake.
RUN gem install --no-rdoc --no-ri rake

# Compass.
RUN gem install --no-rdoc --no-ri compass

# Composer.
RUN wget -q -O /usr/local/bin/composer https://getcomposer.org/composer.phar \
    && chmod +x /usr/local/bin/composer

# Bower, Grunt CLI, Gulp.
RUN npm install --global bower grunt-cli gulp

# Fabric.
RUN apt-get -y install fabric

# Docker Compose (previously Fig).
RUN curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose

# Clean up.
RUN apt-get autoremove --yes \
    && apt-get clean \
    && rm -Rf /var/lib/apt/lists/*


WORKDIR /srv
