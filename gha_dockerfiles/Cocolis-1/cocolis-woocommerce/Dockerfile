FROM --platform=linux/amd64 mysql
FROM wordpress:latest
LABEL Sébastien Fieloux "sebastien.fieloux@gmail.com"
ENV \
    WORDPRESS_ADMIN_USERNAME='admin' \
    WORDPRESS_ADMIN_PASSWORD='admin123' \
    WORDPRESS_ADMIN_EMAIL="admin@example.com" \
    WORDPRESS_URL="127.0.0.1:8189" \
    WORDPRESS_TITLE="My localhost site"

RUN apt-get update && apt-get install -y apt-transport-https
RUN apt-get install -y  unzip wget mariadb-server supervisor sudo

COPY install-plugins.sh /usr/local/bin/install-plugins.sh
COPY wp_post_entrypoint.sh /usr/local/bin/wp_post_entrypoint
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

RUN chmod +x /usr/local/bin/install-plugins.sh &&\
    chmod +x /usr/local/bin/wp_post_entrypoint &&\
    chmod +x /usr/local/bin/docker-entrypoint.sh

RUN cd /tmp && curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && cd &&\
    chmod +x /tmp/wp-cli.phar &&\
    mv /tmp/wp-cli.phar /usr/local/bin/wp

# grr, ENTRYPOINT resets CMD now
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["apache2-foreground"]