FROM wordpress:latest

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Aliases
RUN echo 'alias composer="composer --working-dir=/var/www/html/wp-content/plugins/countdown/src"' >> ~/.bashrc
