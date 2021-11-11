FROM ubuntu:16.04
MAINTAINER Mayel <goto@mayel.space>

# Suppress Upstart errors/warning
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl

# Let the container know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

# doc root path
ENV APP_ROOT="/home/app/"
ENV NGINX_ROOT="/home/app/web"
# display PHP errors
ENV ERRORS=0
# max size of uploads (megabytes)
ENV MAX_UPLOAD=10
# what PHP version to install
ENV IMAGE_PHP_VERSION=7.1

# Update base image
# Add sources for latest nginx & php packages
# Install software requirements
RUN apt-get update && \
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C && \
apt-get install -y software-properties-common apt-utils && \
nginx=stable && \
add-apt-repository ppa:nginx/$nginx && \
LANG=C.UTF-8 add-apt-repository ppa:ondrej/php && \
apt-get update && \
apt-get upgrade -y && \
BUILD_PACKAGES="supervisor sudo unzip nginx git pwgen curl php-apcu php${IMAGE_PHP_VERSION}-fpm php${IMAGE_PHP_VERSION}-mysql php${IMAGE_PHP_VERSION}-pgsql php${IMAGE_PHP_VERSION}-curl php${IMAGE_PHP_VERSION}-gd php${IMAGE_PHP_VERSION}-intl php${IMAGE_PHP_VERSION}-mcrypt php${IMAGE_PHP_VERSION}-sqlite php${IMAGE_PHP_VERSION}-mbstring php${IMAGE_PHP_VERSION}-xml php${IMAGE_PHP_VERSION}-pdo php${IMAGE_PHP_VERSION}-pdo-mysql php${IMAGE_PHP_VERSION}-pdo-pgsql php${IMAGE_PHP_VERSION}-pdo-sqlite php${IMAGE_PHP_VERSION}-cli php${IMAGE_PHP_VERSION}-zip " && \
BUILD_PACKAGES_DISABLED="php${IMAGE_PHP_VERSION}-phalcon php${IMAGE_PHP_VERSION}-mongo php${IMAGE_PHP_VERSION}-memcache php${IMAGE_PHP_VERSION}-tidy php${IMAGE_PHP_VERSION}-xmlrpc php${IMAGE_PHP_VERSION}-xsl php${IMAGE_PHP_VERSION}-ldap" && \
apt-get -y install $BUILD_PACKAGES && \
apt-get remove --purge -y software-properties-common && \
apt-get autoremove -y && \
apt-get clean && \
apt-get autoclean && \
echo -n > /var/lib/apt/extended_states && \
rm -rf /var/lib/apt/lists/* && \
rm -rf /usr/share/man/?? && \
rm -rf /usr/share/man/??_* && \
curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# tweak nginx config
RUN sed -i -e"s/worker_processes  1/worker_processes 5/" /etc/nginx/nginx.conf && \
sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/" /etc/nginx/nginx.conf && \
sed -i -e"s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size ${MAX_UPLOAD}m/" /etc/nginx/nginx.conf && \
echo "daemon off;" >> /etc/nginx/nginx.conf

# tweak php-fpm config
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php/${IMAGE_PHP_VERSION}/fpm/php.ini && \
sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = ${MAX_UPLOAD}M/g" /etc/php/${IMAGE_PHP_VERSION}/fpm/php.ini && \
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = ${MAX_UPLOAD}M/g" /etc/php/${IMAGE_PHP_VERSION}/fpm/php.ini && \
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/${IMAGE_PHP_VERSION}/fpm/php-fpm.conf && \
sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g" /etc/php/${IMAGE_PHP_VERSION}/fpm/pool.d/www.conf && \
sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g" /etc/php/${IMAGE_PHP_VERSION}/fpm/pool.d/www.conf && \
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g" /etc/php/${IMAGE_PHP_VERSION}/fpm/pool.d/www.conf && \
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g" /etc/php/${IMAGE_PHP_VERSION}/fpm/pool.d/www.conf && \
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g" /etc/php/${IMAGE_PHP_VERSION}/fpm/pool.d/www.conf && \
sed -i -e "s/pm.max_requests = 500/pm.max_requests = 200/g" /etc/php/${IMAGE_PHP_VERSION}/fpm/pool.d/www.conf

# fix ownership of sock file for php-fpm
RUN sed -i -e "s/;listen.mode = 0660/listen.mode = 0750/g" /etc/php/${IMAGE_PHP_VERSION}/fpm/pool.d/www.conf && \
find /etc/php/${IMAGE_PHP_VERSION}/cli/conf.d/ -name "*.ini" -exec sed -i -re 's/^(\s*)#(.*)/\1;\2/g' {} \; && \
mkdir /run/php

# nginx site conf
RUN rm -Rf /etc/nginx/conf.d/* && \
rm -Rf /etc/nginx/sites-available/default && \
mkdir -p /etc/nginx/ssl/

COPY ./config/server_nginx.conf.tmpl /etc/nginx/sites-available/default.conf

RUN rm -f /etc/nginx/sites-enabled/default

RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-enabled/default

# Supervisor Config
COPY ./config/supervisord.conf /etc/supervisord.conf

RUN adduser app

# Prepare script
COPY ./config/docker_prepare.sh /
RUN chmod 755 /docker_prepare.sh

# add app files
RUN mkdir -p ${APP_ROOT}
COPY ./ ${APP_ROOT}

RUN chown -Rf app.www-data ${APP_ROOT}
RUN cd ${APP_ROOT} && su app -c "composer install --no-dev --no-interaction -o"

RUN chown -Rf app.www-data ${APP_ROOT}
RUN chmod -Rf 775 ${APP_ROOT}

# Expose Ports
EXPOSE 80
CMD ["/bin/bash", "/docker_prepare.sh"]
# CMD echo "prepare script starting" && /bin/bash /docker_prepare.sh && echo "tailing..." && : >> /docker_prepare.log && tail -f /docker_prepare.log
