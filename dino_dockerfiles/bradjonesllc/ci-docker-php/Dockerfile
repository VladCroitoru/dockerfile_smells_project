FROM php:7.4-cli-buster

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update && apt-get install -yqq --no-install-recommends \
    ca-certificates \
    git \
    wget \
    zip unzip \
    jq \
    patch \
    expect \
    tcl8.6 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=docker:20.10.7 /usr/local/bin/docker /usr/local/bin/

# Install composer.
RUN curl -L -o composer-setup.php https://getcomposer.org/installer \
    && export EXPECTED_CHECKSUM="$(php -r 'copy("https://composer.github.io/installer.sig", "php://stdout");')" \
    && export ACTUAL_CHECKSUM="$(php -r "echo hash_file('sha384', 'composer-setup.php');")" \
    && if [ "$EXPECTED_CHECKSUM" != "$ACTUAL_CHECKSUM" ]; then exit 1; fi \
    && php composer-setup.php \
    && mv composer.phar /usr/local/bin/composer \
    && chmod +x /usr/local/bin/composer \
    && rm composer-setup.php

# Install local PHP security scanning tool.
ENV LOCAL_PHP_SECURITY_CHECKER_VERSION 1.0.0
RUN wget "https://github.com/fabpot/local-php-security-checker/releases/download/v$LOCAL_PHP_SECURITY_CHECKER_VERSION/local-php-security-checker_$LOCAL_PHP_SECURITY_CHECKER_VERSION"_linux_386 \
    && mv local-php-security-checker_"$LOCAL_PHP_SECURITY_CHECKER_VERSION"_linux_386 /usr/local/bin/local-php-security-checker \
    && chmod +x /usr/local/bin/local-php-security-checker

# Install klar.
ENV KLAR_VERSION 2.3.0
RUN curl -o /usr/local/bin/klar -L https://github.com/optiopay/klar/releases/download/v$KLAR_VERSION/klar-$KLAR_VERSION-linux-amd64 \
    && chmod +x /usr/local/bin/klar

# Install Dockerize
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# For maximum compatibility with Symfony console, etc.
RUN ln -s /dev/null /var/log/console \
    && chmod o+rw /var/log/console

COPY *.sh /

RUN useradd -u 2000 -mr runner
ENV HOME /home/runner

VOLUME ["/builds"]

ENTRYPOINT ["/bootstrap.sh"]
