FROM wernight/phantomjs
USER root
RUN apt-get update          &&\
    apt-get -y install        \
        php5-mysql            \
        php5-gd               \
        php5-mcrypt           \
        php5-intl             \
        php5-sqlite           \
        php-apc               \
        php5-memcache         \
        php5-fpm              \
        curl                  \
        wget                  \
        git                   \
        vim                   \
        libcairo2-dev libjpeg62-turbo-dev libpango1.0-dev libgif-dev g++ \
        fontconfig            \
        make                &&\
    apt-get clean autoclean &&\
    apt-get autoremove -y   &&\
    rm -rf /var/lib/{apt,dpkg,cache,log}

RUN sed -i -e "s/;date.timezone =/date.timezone = Europe\/Moscow /i" /etc/php5/cli/php.ini &&\
    sed -i -e "s/;date.timezone =/date.timezone = Europe\/Moscow /i" /etc/php5/fpm/php.ini

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer

EXPOSE 8080

RUN curl -sL https://deb.nodesource.com/setup_5.x | bash - &&\
    apt-get update           &&\
    apt-get -y install         \
           build-essential     \
           nodejs            &&\
    apt-get clean autoclean  &&\
    apt-get autoremove -y    &&\
    rm -rf /var/lib/{apt,dpkg,cache,log}

RUN    npm install -g   \
           bower        \
           gulp         \
           less

RUN ln /usr/bin/node /usr/local/bin/node
RUN ln -s /usr/lib/node_modules /usr/local/lib/

RUN useradd -m -s /bin/bash -u 1000 user


USER user
VOLUME /home/user/.composer
WORKDIR /app
CMD ["./bin/run.sh"]

