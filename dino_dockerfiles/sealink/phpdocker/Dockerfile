FROM ubuntu:16.04

# Suppress Upstart errors/warning
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl

# Let the container know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

# Add sources for latest nginx
RUN apt-get clean && apt-get update && apt-get install -y wget
RUN wget -q http://nginx.org/keys/nginx_signing.key -O- | apt-key add -
RUN echo deb http://nginx.org/packages/mainline/ubuntu/ trusty nginx >> /etc/apt/sources.list
RUN echo deb-src http://nginx.org/packages/mainline/ubuntu/ trusty nginx >> /etc/apt/sources.list

# Update System
RUN apt-get update
RUN apt-get -y upgrade

# Install Basic Requirements
RUN apt-get -y install nginx python-software-properties python-setuptools software-properties-common curl vim zip unzip git

# Language
RUN apt-get -y install language-pack-en-base
RUN export LC_ALL=en_US.UTF-8
RUN export LANG=en_US.UTF-8

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C
RUN LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php
RUN apt-get update

# Install PHP
RUN apt-get -y install php7.0-fpm php7.0-cli php7.0-dev php7.0-common \
    php7.0-json php7.0-opcache php7.0-readline php7.0-mbstring php7.0-curl \
    php-imagick php7.0-mcrypt php7.0-mysql php7.0-xml php-redis

RUN apt-get -y autoremove
# Install Composer
RUN curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer && \
    # generate accesskey for app https://github.com/organizations/sealink/settings/applications/308702
    composer config -g github-oauth.github.com 8e52e76a7ff35c03076f0d2382ad205b5a06f42f

# yarn package manager
RUN apt-key adv --fetch-keys http://dl.yarnpkg.com/debian/pubkey.gpg && \
    echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
# Add Node sources and apt-get update
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \
    apt-get install -y build-essential nodejs yarn

# Clean
RUN apt-get clean && rm -r /var/lib/apt/lists/*

# tweak nginx config
# gets over written by start.sh to match cpu's on container
RUN sed -i -e"s/worker_processes 1/worker_processes 5/" /etc/nginx/nginx.conf && \
    sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/" /etc/nginx/nginx.conf && \
    sed -i -e"s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size 100m/" /etc/nginx/nginx.conf && \
    sed -i "s/.*conf\.d\/\*\.conf;.*/&\n    include \/etc\/nginx\/sites-enabled\/\*;/" /etc/nginx/nginx.conf && \
    # Change to root for mounting of local files.
    echo "daemon off;" >> /etc/nginx/nginx.conf && \
    # Add font types
    sed -i -e "s@}@application/x-font-ttf ttf; font/opentype otf; application/vnd.ms-fontobject eot; font/x-woff woff;}@g" /etc/nginx/mime.types

# tweak php-fpm config
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php/7.0/fpm/php.ini  && \
    sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 30M/g" /etc/php/7.0/fpm/php.ini && \
    sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 30M/g" /etc/php/7.0/fpm/php.ini && \
    sed -i -e "s/memory_limit\s*=\s*128M/memory_limit = 256M/g" /etc/php/7.0/fpm/php.ini && \
    sed -i -e 's/variables_order = "GPCS"/variables_order = "EGPCS"/' /etc/php/7.0/fpm/php.ini && \
    sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.0/fpm/php-fpm.conf && \
    sed -i -e "s@pid = /run/php/php7.0-fpm.pid@pid = /var/run/php7.0-fpm.pid@g" /etc/php/7.0/fpm/php-fpm.conf && \
    sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g" /etc/php/7.0/fpm/pool.d/www.conf && \
    sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g" /etc/php/7.0/fpm/pool.d/www.conf && \
    sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g" /etc/php/7.0/fpm/pool.d/www.conf && \
    sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g" /etc/php/7.0/fpm/pool.d/www.conf && \
    sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g" /etc/php/7.0/fpm/pool.d/www.conf && \
    sed -i -e "s/^;clear_env = no$/clear_env = no/" /etc/php/7.0/fpm/pool.d/www.conf && \
    sed -i -e "s/pm.max_requests = 500/pm.max_requests = 200/g" /etc/php/7.0/fpm/pool.d/www.conf


# fix ownership of sock file for php-fpm as our version of nginx runs as nginx
RUN sed -i -e "s/user = www-data/user = nginx/g" /etc/php/7.0/fpm/pool.d/www.conf && \
    sed -i -e "s/group = www-data/group = nginx/g" /etc/php/7.0/fpm/pool.d/www.conf && \
    sed -i -e "s/listen.owner = www-data/listen.owner = nginx/g" /etc/php/7.0/fpm/pool.d/www.conf && \
    sed -i -e "s/listen.group = www-data/listen.group = nginx/g" /etc/php/7.0/fpm/pool.d/www.conf && \
    sed -i -e "s/;listen.mode = 0660/listen.mode = 0750/g" /etc/php/7.0/fpm/pool.d/www.conf && \
    sed -i -e "s@listen = /run/php/php7.0-fpm.sock@listen = /var/run/php7.0-fpm.sock@g" /etc/php/7.0/fpm/pool.d/www.conf && \
    find /etc/php/7.0/cli/conf.d/ -name "*.ini" -exec sed -i -re 's/^(\s*)#(.*)/\1;\2/g' {} \;

# nginx site conf
RUN rm -Rf /etc/nginx/conf.d/* && \
    mkdir -p /etc/nginx/sites-available/ && \
    mkdir -p /etc/nginx/sites-enabled/ && \
    mkdir -p /etc/nginx/ssl/ && \
    mkdir -p /etc/nginx/site-includes

ADD ./nginx-site.conf /etc/nginx/sites-available/default.conf
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-enabled/default.conf


# setup nginx public dir
RUN mkdir -p /app/public
ADD index.php /app/public/index.php
# RUN chown -Rf nginx:nginx /app/public

# Supervisor Config
RUN /usr/bin/easy_install supervisor
RUN /usr/bin/easy_install supervisor-stdout
ADD ./supervisord.conf /etc/supervisord.conf

# Start Supervisord
ADD ./start.sh /start.sh
RUN chmod 755 /start.sh

# Expose Ports
EXPOSE 443
EXPOSE 80


CMD ["/start.sh"]
