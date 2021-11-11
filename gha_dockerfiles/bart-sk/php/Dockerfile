FROM bartsk/alpine:v1.0.5
RUN apk add php7 \
            php7-curl \
            php7-mbstring \
            php7-iconv \
            php7-openssl \
            php7-json \
            php7-phar \
            php7-mcrypt \ 
            php7-pdo \
            php7-dom \
            php7-tokenizer \
            php7-session \
            php7-ctype \
            php7-xml \
            php7-xmlwriter \
            php7-zip \
            php7-gd \
            php7-simplexml \
            php7-xmlreader \
            sshfs \
            rsync \
            curl && \
            curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer


ADD ./php.ini /etc/php7/php.ini

ADD ./sshfs-deploy.sh /root