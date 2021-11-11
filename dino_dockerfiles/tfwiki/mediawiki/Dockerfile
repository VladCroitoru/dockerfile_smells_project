FROM mediawiki:1.31

# Luxuries
RUN apt-get update && apt-get install -y \
        vim \
        less \
        zip \
        unzip \
        libmemcached-dev \
        libz-dev \
    --no-install-recommends && \
    rm -r /var/lib/apt/lists/*

RUN curl -sS https://getcomposer.org/installer | \
    php -- --install-dir=/usr/bin/ --filename=composer

# We want Apache's rewrite module
RUN a2enmod rewrite
RUN a2enmod headers

# MediaWiki needs these extra extensions
RUN docker-php-ext-install sockets
RUN pecl install memcached && \
    docker-php-ext-enable memcached

# We want the wiki in a w/ subfolder
RUN mv /var/www/html /var/www/i-will-be-w && \
    mkdir -p /var/www/html && \
    mv /var/www/i-will-be-w /var/www/html/w

# Assets
COPY src/fonts /var/www/html/fonts
COPY src/favicon.ico /var/www/html/

# Shell utils
COPY src/shell /var/www/html/shell

# Scripts
COPY src/scripts /var/www/html/scripts

# Valve skin
# TODO: Check how much of this is actually used, and clean up
COPY src/skins/valve /var/www/html/w/skins/valve

# MediaWiki extensions
COPY src/extensions/AbuseFilter /var/www/html/w/extensions/AbuseFilter
COPY src/extensions/Buggy /var/www/html/w/extensions/Buggy
COPY src/extensions/CheckUser /var/www/html/w/extensions/CheckUser
COPY src/extensions/Echo /var/www/html/w/extensions/Echo
COPY src/extensions/EmbedVideo /var/www/html/w/extensions/EmbedVideo
COPY src/extensions/Flow /var/www/html/w/extensions/Flow
COPY src/extensions/NewUserMessage /var/www/html/w/extensions/NewUserMessage
COPY src/extensions/RedditThumbnail /var/www/html/w/extensions/RedditThumbnail
COPY src/extensions/Scribunto /var/www/html/w/extensions/Scribunto
COPY src/extensions/Sentry /var/www/html/w/extensions/Sentry
COPY src/extensions/Thanks /var/www/html/w/extensions/Thanks
COPY src/extensions/UserMerge /var/www/html/w/extensions/UserMerge
COPY src/extensions/Nuke /var/www/html/w/extensions/Nuke

RUN composer install --no-dev --working-dir=/var/www/html/w/extensions/AbuseFilter
RUN composer install --no-dev --working-dir=/var/www/html/w/extensions/CheckUser
RUN composer install --no-dev --working-dir=/var/www/html/w/extensions/Echo
RUN composer install --no-dev --working-dir=/var/www/html/w/extensions/Flow
RUN composer install --no-dev --working-dir=/var/www/html/w/extensions/Sentry

# Better Scribunto (lua) performance, apparently
COPY ext/luasandbox /opt/luasandbox
RUN apt-get update && apt-get install -y liblua5.1-0-dev
RUN ( \
    cd /opt/luasandbox; \
    phpize; \
    ./configure; \
    make; \
    make install \
)
RUN docker-php-ext-enable luasandbox

# Generate config at runtime
COPY scripts/configure-mediawiki.sh /usr/local/bin/configure-mediawiki
COPY scripts/configure-blackfire.sh /usr/local/bin/configure-blackfire
RUN chmod +x /usr/local/bin/configure-*

# Config templates
COPY configs/php.ini /usr/local/etc/php/php.ini
COPY configs/apache.conf /etc/apache2/sites-available/000-default.conf
COPY configs/LocalSettings.php /var/www/html/w/LocalSettings.php

# Any well known gubbins
COPY src/.well-known /var/www/html/.well-known

VOLUME /var/www/html/w/images

# Required environmental variables
ENV DB_DATABASE='wiki'
ENV DB_HOST='db'
ENV DB_TYPE='mysql'
ENV DB_USER='root'
ENV RECAPTCHA_KEY=
ENV RECAPTCHA_SECRET=
ENV SECRET_KEY=
ENV SERVER_URL='https://tfwiki.localhost'
ENV SITENAME='Local Team Fortress Wiki'

# Optional environmental variables
ENV BLACKFIRE_SOCKET=
ENV DB_PASSWORD=
ENV EMAIL_EMERGENCY_CONTACT=
ENV EMAIL_PASSWORD_SENDER=
ENV MEMCACHED_HOST=
ENV READ_ONLY_MESSAGE=
ENV SENTRY_DSN=
ENV SMTP_AUTH=
ENV SMTP_HOST=
ENV SMTP_IDHOST=
ENV SMTP_PASSWORD=
ENV SMTP_PORT=
ENV SMTP_USERNAME=
ENV STEAM_API_KEY=
ENV TRUSTED_PROXIES=
ENV VARNISH_HOST=

CMD /usr/local/bin/configure-blackfire && /usr/local/bin/configure-mediawiki && apache2-foreground
