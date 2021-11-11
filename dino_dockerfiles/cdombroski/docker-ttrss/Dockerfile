FROM smebberson/alpine-nginx
ENV SELF_URL_PATH=http://localhost/ DB_HOST=db DB_PORT=5432 DB_USER=ttrss \
DB_PASS=ttrss DB_NAME=ttrss
ADD rootfs /
RUN apk add --no-cache git php php-pgsql php-fpm php-cli php-curl php-gd \
php-intl php-json php-mcrypt php-dom php-pcntl php-posix php-pdo_pgsql
RUN rm /usr/html/index.html && \
git clone https://git.tt-rss.org/git/tt-rss.git /usr/html && \
chgrp -R www-data /usr/html && \
chmod -R g+w /usr/html/cache /usr/html/feed-icons /usr/html/lock
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
ln -sf /dev/stderr /var/log/nginx/error.log && \
sed -i -e 's/;daemonize\s*=\s*yes/daemonize = no/' /etc/php/php-fpm.conf && \
sed -i -e 's@listen\s*=.*@listen = /var/run/php-fpm.sock@' /etc/php/php-fpm.conf && \
sed -i -e 's@;listen\.owner\s*=.*@listen.owner = nginx@' /etc/php/php-fpm.conf && \
sed -i -e 's@group\s*=.*@group = www-data@' /etc/php/php-fpm.conf
