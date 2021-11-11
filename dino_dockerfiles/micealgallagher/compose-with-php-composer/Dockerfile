FROM tmaier/docker-compose

# Configuration
ENV EDGE_REPO "http://dl-4.alpinelinux.org/alpine/edge/testing"
ENV COMPOSER_DEPENDENCIES "wget curl git php7 php7-curl php7-openssl php7-json php7-phar php7-dom php7-mbstring php7-zlib php7-tokenizer"

# Add Edge repo
RUN apk --update --repository=$EDGE_REPO add
# Install Composer dependencies
RUN apk --update add $COMPOSER_DEPENDENCIES
# Clear the APK cache
RUN rm /var/cache/apk/*
# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer
