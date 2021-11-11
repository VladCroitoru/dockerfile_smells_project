FROM nginx

MAINTAINER mdestombes

# Install required packages and remove the apt packages cache when done.
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    	cron \
    	logrotate \
        nano \
        php-fpm \
        && \
    rm -rf /var/lib/apt/lists/*

# Congiguration dir
RUN mkdir  /home/config/

# Copy launcher
COPY run.sh /home/config/run.sh
RUN chmod 777 /home/config/run.sh

# Copy basic install
COPY index.php /home/config/index.php
COPY error.html /home/config/error.html

# Copy basic logrotate configuration
COPY logrotate /home/config/logrotate

WORKDIR /home/web/

# Add to sudo group
RUN usermod -a -G www-data nginx

# NGINX Configuration
COPY nginx.default.conf /home/config/nginx.default.conf

# PHP Configuration
COPY www.php.ini /home/config/www.php.ini
COPY www.php.conf /home/config/www.php.conf

EXPOSE 80

# Update game launch the game.
ENTRYPOINT ["/home/config/run.sh"]
