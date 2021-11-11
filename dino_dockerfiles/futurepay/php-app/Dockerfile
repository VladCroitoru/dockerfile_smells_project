FROM php:7.1.4-apache

COPY assets/* /tmp/

# Install pdo
RUN docker-php-ext-install pdo_mysql

# Enable mod_rewrite
RUN a2enmod rewrite

# Install confd
RUN curl -Lo /usr/local/bin/confd https://github.com/kelseyhightower/confd/releases/download/v0.15.0/confd-0.15.0-linux-amd64 && \
    chmod +x /usr/local/bin/confd && \
    mkdir -p /etc/confd/templates && \
    mkdir -p /etc/confd/conf.d

# Install aws-env
RUN curl -Lo /usr/local/bin/aws-env https://github.com/Droplr/aws-env/raw/872ca7e45a8fdc519ff40745c56175ae81d3b66b/bin/aws-env-linux-amd64 && \
    chmod +x /usr/local/bin/aws-env

# Install entrypoint
RUN mv /tmp/entrypoint /usr/local/bin/

# Cleanup
RUN rm -r /tmp/*

WORKDIR /var/www
ENTRYPOINT ["entrypoint"]
CMD ["apache2-foreground"]
