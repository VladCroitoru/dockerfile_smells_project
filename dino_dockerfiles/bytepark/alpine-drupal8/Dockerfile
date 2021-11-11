FROM bytepark/alpine-nginx-php7:latest
MAINTAINER bytepark GmbH <code@bytepark.de>

# Add some tools
RUN apk upgrade -U && \
    apk add 'tar=1.28-r1' --update-cache --repository http://nl.alpinelinux.org/alpine/v3.3/main && \
    apk --update --repository=http://dl-4.alpinelinux.org/alpine/edge/testing add \
    php7-zlib \
    php7-gd \
    php7-session \
    php7-sqlite3 \
    php7-mysqlnd \
    php7-pdo_sqlite \
    git \
    gzip \
    ca-certificates \
    mysql-client \
    openssh \
    imagemagick

COPY /rootfs /

RUN chown root:root /usr/local/bin/fixperm.sh && \
    chmod 700 /usr/local/bin/fixperm.sh

# Install drush
RUN wget -O /usr/local/bin/drush http://files.drush.org/drush.phar && chmod 700 /usr/local/bin/drush

## download drupal
RUN cd /tmp && \
    drush dl drupal --drupal-project-rename=drupal && \
    rm -rf /usr/share/nginx/html && \
    mv -f /tmp/drupal /usr/share/nginx/html && \
    mv /usr/share/nginx/html/sites/default /usr/share/nginx/html/sites/default.init

RUN fixperm.sh

VOLUME ["/usr/share/nginx/html/sites"]
VOLUME ["/usr/share/nginx/html/modules"]
VOLUME ["/usr/share/nginx/html/profiles"]
VOLUME ["/usr/share/nginx/html/themes"]
VOLUME ["/usr/share/nginx/backup"]

WORKDIR /usr/share/nginx/html

ENTRYPOINT ["/init"]