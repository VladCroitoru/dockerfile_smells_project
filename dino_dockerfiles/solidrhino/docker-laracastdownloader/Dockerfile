FROM php:7.0-cli
ENV COMPOSER_HOME="/app"

#Add your email and password on runtime
ENV EMAIL = ""
ENV PASSWORD = ""

ADD start.sh /start.sh

# Make directory
RUN mkdir -p /downloads && \

# install dependences
apt-get update && apt-get install -y libcurl4-gnutls-dev zlib1g-dev git && \
docker-php-ext-configure curl --with-curl && \
docker-php-ext-install -j$(nproc) curl zip

# Install laravel downloader
RUN git clone https://github.com/iamfreee/laracasts-downloader.git /app && \
cd /app && \
curl --silent --show-error https://getcomposer.org/installer | php && \
php composer.phar install && \
mv /app/.env.example /app/.env && \
chmod +x /start.sh && \
rm -rf /var/cache/apk/* /tmp/* /var/tmp/*

VOLUME /downloads

ENTRYPOINT ["/start.sh"]
