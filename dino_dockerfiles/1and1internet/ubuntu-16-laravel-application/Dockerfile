FROM 1and1internet/ubuntu-16-nginx-php-7.1
MAINTAINER brian.wojtczak@1and1.co.uk
ARG DEBIAN_FRONTEND=noninteractive
COPY files /
ENV \
    DOCUMENT_ROOT=html/public \
    APP_WORKER_QUEUES=high,low \
    APP_WORKER_TIMEOUT=180 \
    WAIT_FOR_DB_MIGRATIONS=prompt
RUN \
    apt-get update -q && \
    apt-get install -q -o Dpkg::Options::=--force-confdef -y php7.1-bcmath php7.1-gmp php7.1-json php7.1-ldap php7.1-recode php7.1-pspell php7.1-soap php7.1-bz2 && \
    apt-get install -q -o Dpkg::Options::=--force-confdef -y sqlite3 libmysqlclient-dev mysql-common mysql-client && \
    apt-get install -q -o Dpkg::Options::=--force-confdef -y ca-certificates openssl-blacklist ssl-cert apache2-utils python-pip && \
    apt-get autoremove -q -y && \
    apt-get clean -q -y && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/www/html && \
    rm -rf /var/www && \
    rm -rf /var/log/nginx/*.log && \
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stdout /var/log/php7.1-fpm.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log && \
    sed -i -e 's/access_log .*;$/access_log \/var\/log\/nginx\/access\.log;/g' /etc/nginx/sites-enabled/site.conf && \
    sed -i -e 's/error_log .*;$/error_log stderr;/g' /etc/nginx/sites-enabled/site.conf && \
    chmod 666 /var/log/php7.1-fpm.log /var/log/nginx/*.log && \
    sed -i -e 's/;clear_env = no/clear_env = no/g' /etc/php/7.1/fpm/pool.d/*.conf && \
    mv /etc/supervisor/conf.d /etc/supervisor/conf.d.template && \
    mkdir -p /etc/supervisor/conf.d && \
    chmod -R 777 /etc/supervisor/conf* && \
    chmod -R 755 /hooks/supervisord-pre.d/* && \
    mkdir -p /var/www/html && \
    composer create-project \
    --no-ansi \
    --no-dev \
    --no-interaction \
    --no-progress \
    --prefer-dist \
    laravel/laravel /var/www/html ~5.2.0 && \
    ln -sf /var/www/html/artisan /usr/bin/artisan && \
    chmod 755 /var/www/html/artisan && \
    touch /var/www/html/storage/logs/laravel.log && \
    chmod 666 /var/www/html/storage/logs/laravel.log && \
    rm -f /var/www/html/database/migrations/*.php /var/www/html/app/Users.php && \
    chmod 666 /etc/nginx/sites-enabled/* /etc/passwd /etc/group && \
    application-set-file-permissions
WORKDIR /var/www/html
CMD ["application-all"]
ONBUILD RUN php artisan --no-ansi --no-interaction key:generate
