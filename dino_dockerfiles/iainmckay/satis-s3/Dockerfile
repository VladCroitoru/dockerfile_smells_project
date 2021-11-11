FROM php:5-cli

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get install -yq --no-install-recommends python-pip git zlib1g-dev openssh-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/* \
    && pip install awscli

RUN docker-php-ext-install zip

RUN echo "date.timezone = UTC" >> /usr/local/etc/php/php.ini \
	&& curl -sS https://getcomposer.org/installer | php \
	&& php composer.phar create-project composer/satis --stability=dev \
	&& ln /satis/bin/satis /usr/local/bin

RUN mkdir ~/.ssh \
	&& ssh-keyscan -H bitbucket.org >> /root/.ssh/known_hosts \
	&& ssh-keyscan -H github.com >> /root/.ssh/known_hosts

ADD run.sh /run.sh

CMD [ "/run.sh", "/satis/bin/satis", "/config.json", "/tmp/satis" ]