FROM tutum/apache-php

RUN apt-get update
RUN apt-get install -y \
    wget \
    php5-intl \
    php5-mcrypt

RUN php5enmod mcrypt

RUN a2enmod rewrite

RUN echo "date.timezone = \"Asia/Dubai\"" >> /etc/php5/cli/php.ini && \
    echo "date.timezone = \"Asia/Dubai\"" >> /etc/php5/apache2/php.ini

# Set Default Variables
ENV PIM_VERSION 1.2.7

RUN rm -rf /app && \
    mkdir -p /src && \
    wget -P /src https://github.com/akeneo/pim-community-standard/archive/v${PIM_VERSION}.tar.gz && \
    tar -C /src -xvzf /src/v${PIM_VERSION}.tar.gz --strip-components 1 && \
    rm /src/v${PIM_VERSION}.tar.gz

WORKDIR /src

RUN composer config -g github-oauth.github.com 0e22a79af5acecd53ec1fc33cd300667c233f3f1 && \
    composer install --prefer-dist 

ADD ./sites-enabled/akeneo-pim.conf /etc/apache2/sites-enabled/000-default.conf
ADD ./run.sh /run.sh
RUN chmod +x /run.sh

RUN rm -rf /src/app/cache/* && \
    rm -fr /src/app/logs/* && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    find /var/log -type f | while read f; do echo -ne '' > $f; done; \
    ln -sf /dev/stdout /var/log/apache2/access.log && \
    ln -sf /dev/stderr /var/log/apache2/error.log

EXPOSE 80

CMD ["/run.sh"]
