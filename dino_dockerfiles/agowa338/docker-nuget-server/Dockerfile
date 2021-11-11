FROM nginx
MAINTAINER agowa338

ENV APP_BASE /var/www/simple-nuget-server
ENV DEFAULT_SIZE 20M
ENV DEFAULT_WORKER_PROCESSES 1
ENV DEFAULT_WORKER_CONNECTIONS 65535

# Copy simple-nuget-server into the container
COPY simple-nuget-server $APP_BASE

# Install PHP7 && Download project
RUN apt-get update && \
    apt-get install -y --no-install-recommends --no-install-suggests \
    ca-certificates php php-fpm php-sqlite3 php-zip php-xml curl && \
    rm -rf /var/lib/apt/lists/* && \
    chown www-data:www-data $APP_BASE/db $APP_BASE/packagefiles && \
    chmod 0770 $APP_BASE/db $APP_BASE/packagefiles && \
    rm /etc/nginx/conf.d/* && \
    usermod -aG www-data nginx

# Activate the nginx configuration
COPY nginx.conf.example /etc/nginx/conf.d/nuget.conf.example
COPY nginx.conf.tlsexample /etc/nginx/conf.d/nugettls.conf.example

COPY docker-entrypoint /bin/docker-entrypoint

# Set default upload file sizes limit
RUN sed -i -e "s/post_max_size.*/post_max_size = $DEFAULT_SIZE/" /etc/php/7.3/fpm/php.ini && \
    sed -i -e "s/upload_max_filesize.*/upload_max_filesize = $DEFAULT_SIZE/" /etc/php/7.3/fpm/php.ini && \
    sed -i -e "s/;pm.max_requests.*$/pm.max_requests = 10240/" /etc/php/7.3/fpm/pool.d/www.conf && \
    sed -i -e "s/client_max_body_size.*$/client_max_body_size $DEFAULT_SIZE;/g" /etc/nginx/conf.d/nuget.conf.example && \
    sed -i -e "s/client_max_body_size.*$/client_max_body_size $DEFAULT_SIZE;/g" /etc/nginx/conf.d/nugettls.conf.example && \
    sed -i -e "s/worker_processes.*$/worker_processes  $DEFAULT_WORKER_PROCESSES;/" /etc/nginx/nginx.conf && \
    sed -i -e "s/worker_connections.*$/    worker_connections  $DEFAULT_WORKER_CONNECTIONS ;/" /etc/nginx/nginx.conf && \
    sed -i -e "/worker_connections.*$/a\    use epoll;" /etc/nginx/nginx.conf && \
    sed -i -e "s/keepalive_timeout.*$/    keepalive_timeout  5;/" /etc/nginx/nginx.conf && \
    chmod +x /bin/docker-entrypoint

HEALTHCHECK --interval=5m --timeout=3s CMD curl --output /dev/null --fail --silent http://localhost/status.php || curl --output /dev/null --fail --silent https://localhost/status.php || exit 1

VOLUME ["$APP_BASE/db", "$APP_BASE/packagefiles", "/etc/nginx/tls"]

EXPOSE 80 443

ENTRYPOINT ["docker-entrypoint"]
