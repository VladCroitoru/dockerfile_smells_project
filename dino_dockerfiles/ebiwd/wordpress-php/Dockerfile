FROM wodby/drupal-php:5.6

RUN rm -rf /home/www-data/.composer && \
    apk add --no-cache less ncurses && \
    curl -o /usr/local/bin/wp https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && \
    chmod +x /usr/local/bin/wp
