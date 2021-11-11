FROM pam79/php-fpm:v7.4.1
LABEL maintainer="Abdullah Morgan <paapaabdullahm@gmail.com>"

# Add Tini init
ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

# Add Composer
RUN apt update && apt install -y bash curl git openssh-server openssl zip unzip; \
    #
    # Download the installer to the current directory
    php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"; \
    #
    # Verify the installer SHA-384
    php -r "if (hash_file('SHA384', 'composer-setup.php') === \
        'c5b9b6d368201a9db6f74e2611495f369991b72d9c8cbd3ffbc63edff210eb73d46ffbfce88669ad33695ef77dc76976') \
        { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"; \
    #
    # Run the installer
    php composer-setup.php; \
    #
    # Make binary globally accessible
    mv composer.phar /usr/bin/composer; \
    #
    # Clean up
    php -r "unlink('composer-setup.php');";

COPY docker-entrypoint.sh /docker-entrypoint.sh

WORKDIR /src
VOLUME /src

ENTRYPOINT ["/bin/sh", "/docker-entrypoint.sh"]
CMD ["composer"]
