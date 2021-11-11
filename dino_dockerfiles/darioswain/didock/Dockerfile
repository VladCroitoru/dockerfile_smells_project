FROM php:7-cli
COPY . /usr/src/didock
WORKDIR /usr/src/didock
RUN apt-get update && \
    apt-get install -y git zlib1g-dev && \
    docker-php-ext-install -j$(nproc) mbstring fileinfo zip && \
    php -r "readfile('https://getcomposer.org/installer');" > composer-setup.php && \
    php composer-setup.php --install-dir=/usr/src/didock --filename=composer --version=1.0.0 && \
    php -r "unlink('composer-setup.php');" && \
    cd /usr/src/didock && php /usr/src/didock/composer install --no-dev && \
    apt-get remove -y git && apt-get clean -y && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*
ENTRYPOINT ["bin/didock"]
