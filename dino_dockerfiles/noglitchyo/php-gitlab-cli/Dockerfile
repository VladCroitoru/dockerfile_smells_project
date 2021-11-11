FROM php:7.1-cli

LABEL maintainer="Maxime Elomari <maxime.elomari@gmail.com>"
LABEL description="A simple tool made to query your preferred Gitlab API from the command line."

ENV REPOSITORY https://github.com/noglitchyo/php-gitlab-cli.git
ENV SOURCES_URL https://github.com/noglitchyo/php-gitlab-cli/archive/master.zip
ENV WORKDIR /opt/php-gitlab-cli
ENV GITLAB_TOKEN ""
ENV GITLAB_URL ""

RUN apt-get update && apt-get install -y curl zip

WORKDIR $WORKDIR

ADD bin/ bin/
ADD src/ src/
ADD config/ config/
ADD composer.json composer.json
ADD bootstrap.php bootstrap.php
RUN chmod +x bin/console

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php -r "if (hash_file('SHA384', 'composer-setup.php') === '544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
    && php composer-setup.php --filename=composer \
    && php -r "unlink('composer-setup.php');" \
    && mv composer /usr/local/bin/composer \
    && composer install --prefer-dist --no-dev

ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENTRYPOINT ["/docker-entrypoint.sh"]
