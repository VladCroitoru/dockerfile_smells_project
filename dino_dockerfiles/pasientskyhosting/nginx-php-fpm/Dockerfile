FROM debian:jessie-slim

MAINTAINER Andreas Krüger <ak@patientsky.com>

ENV php_conf /etc/php/7.1/fpm/php.ini
ENV fpm_conf /etc/php/7.1/fpm/pool.d/www.conf
ENV DEBIAN_FRONTEND noninteractive
ENV composer_hash 55d6ead61b29c7bdee5cccfb50076874187bd9f21f65d8991d46ec5cc90518f447387fb9f76ebae1fbbacf329e583e30

RUN apt-get update \
    && apt-get install -y -q --no-install-recommends \
    apt-transport-https \
    lsb-release \
    wget \
    apt-utils \
    ca-certificates

RUN echo "deb http://nginx.org/packages/debian/ jessie nginx" > /etc/apt/sources.list.d/nginx.list && \
    echo "deb-src http://nginx.org/packages/debian/ jessie nginx" >> /etc/apt/sources.list.d/nginx.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ABF5BD827BD9BF62

RUN echo "deb http://packages.dotdeb.org jessie all" > /etc/apt/sources.list.d/dotdeb.list && \
    echo "deb-src http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list.d/dotdeb.list && \
    wget https://www.dotdeb.org/dotdeb.gpg && apt-key add dotdeb.gpg

RUN wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg && \
    echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/php.list

RUN echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' | tee /etc/apt/sources.list.d/newrelic.list && \
    wget -O- https://download.newrelic.com/548C16BF.gpg | apt-key add -

RUN apt-get update \
    && apt-get install -y -q --no-install-recommends \
    php7.1-cli \
    php7.1-fpm \
    php7.1-mysql \
    php7.1-bcmath \
    php7.1-gd \
    php7.1-curl \
    php7.1-json \
    php7.1-mcrypt \
    php7.1-cli \
    php7.1-apcu \
    php7.1-imagick \
    php7.1-intl \
    php7.1-opcache \
    php7.1-mongodb \
    php7.1-mbstring \
    php7.1-xml \
    php7.1-zip \
    php-igbinary \
    php-amqp \
    nginx \
    supervisor \
    openssh-client \
    unzip \
    newrelic-php5 \
    newrelic-sysmond \
    git \
    && apt-get clean \
    && rm -r /var/lib/apt/lists/*

RUN mkdir -p /etc/nginx && \
    mkdir -p /var/www/app && \
    mkdir -p /run/nginx && \
    mkdir -p /var/log/supervisor

ADD conf/supervisord.conf /etc/supervisord.conf

# Copy our nginx config
RUN rm -Rf /etc/nginx/nginx.conf
ADD conf/nginx.conf /etc/nginx/nginx.conf

# RUN useradd -ms /bin/bash nginx

# nginx site conf
RUN mkdir -p /etc/nginx/sites-available/ && \
mkdir -p /etc/nginx/sites-enabled/ && \
rm -Rf /etc/nginx/sites-available/* && \
rm -Rf /etc/nginx/sites-enabled/* && \
rm -Rf /var/www/* && \
mkdir /var/www/html/

ADD conf/nginx-site.conf /etc/nginx/sites-available/default.conf
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-enabled/default.conf

# tweak php and php-fpm config
RUN sed -i \
        -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" \
        -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g" \
        -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g" \
        -e "s/variables_order = \"GPCS\"/variables_order = \"EGPCS\"/g" \
        -e "s/;error_log\s*=\s*syslog/error_log = \/tmp\/logpipe/g" \
        -e "s/memory_limit\s*=\s*128M/memory_limit = 3072M/g" \
        -e "s/;date.timezone\s*=/date.timezone = Europe\/Oslo/g" \
        -e "s/max_execution_time\s*=\s*30/max_execution_time = 300/g" \
        -e "s/max_input_time\s*=\s*60/max_input_time = 300/g" \
        -e "s/default_socket_timeout\s*=\s*60/default_socket_timeout = 300/g" \
        ${php_conf} && \
    sed -i \
        -e "s/;events.mechanism\s*=\s*epoll/events.mechanism = epoll/g" \
        -e "s/;emergency_restart_threshold\s*=\s*0/emergency_restart_threshold = 3/g" \
        -e "s/;emergency_restart_interval\s*=\s*0/emergency_restart_interval = 1m/g" \
        -e "s/;process_control_timeout\s*=\s*0/process_control_timeout = 5s/g" \
        -e "s/error_log\s*=\s*\/var\/log\/php7.1-fpm.log/error_log = \/tmp\/logpipe/g" \
        /etc/php/7.1/fpm/php-fpm.conf && \
    sed -i \
        -e "s/;daemonize\s*=\s*yes/daemonize = no/g" \
        -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g" \
        -e "s/pm.max_children = 4/pm.max_children = 4/g" \
        -e "s/pm.start_servers = 2/pm.start_servers = 3/g" \
        -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g" \
        -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g" \
        -e "s/;pm.max_requests = 500/pm.max_requests = 200/g" \
        -e "s/user = www-data/user = nginx/g" \
        -e "s/group = www-data/group = nginx/g" \
        -e "s/;listen.owner = www-data/listen.owner = nginx/g" \
        -e "s/;listen.group = www-data/listen.group = nginx/g" \
        -e "s/listen = \/run\/php\/php7.1-fpm.sock/listen = \/var\/run\/php-fpm.sock/g" \
        -e "s/^;clear_env = no$/clear_env = no/" \
        ${fpm_conf}

# Cleanup some files and remove comments
RUN find /etc/php/7.1/fpm/conf.d -name "*.ini" -exec sed -i -re '/^[[:blank:]]*(\/\/|#|;)/d;s/#.*//' {} \; && \
    find /etc/php/7.1/fpm/conf.d -name "*.ini" -exec sed -i -re '/^$/d' {} \; && \
    find /etc/php/7.1/fpm/pool.d -name "*.conf" -exec sed -i -re '/^[[:blank:]]*(\/\/|#|;)/d;s/#.*//' {} \; && \
    find /etc/php/7.1/fpm/pool.d -name "*.conf" -exec sed -i -re '/^$/d' {} \; && \
    find /etc/php/7.1/cli/conf.d -name "*.ini" -exec sed -i -re '/^[[:blank:]]*(\/\/|#|;)/d;s/#.*//' {} \; && \
    find /etc/php/7.1/cli/conf.d -name "*.ini" -exec sed -i -re '/^$/d' {} \; && \
    find /etc/php/7.1/fpm/ -name "*.conf" -exec sed -i -re '/^[[:blank:]]*(\/\/|#|;)/d;s/#.*//' {} \; && \
    find /etc/php/7.1/fpm/ -name "*.conf" -exec sed -i -re '/^$/d' {} \;

# Configure php opcode cache
RUN echo "opcache.enable=1" >> /etc/php/7.1/fpm/conf.d/10-opcache.ini && \
    echo "opcache.enable_cli=1" >> /etc/php/7.1/fpm/conf.d/10-opcache.ini && \
    echo "opcache.validate_timestamps=0" >> /etc/php/7.1/fpm/conf.d/10-opcache.ini && \
    echo "opcache.max_accelerated_files=1000000" >> /etc/php/7.1/fpm/conf.d/10-opcache.ini && \
    echo "opcache.memory_consumption=1024" >> /etc/php/7.1/fpm/conf.d/10-opcache.ini && \
    echo "opcache.interned_strings_buffer=8" >> /etc/php/7.1/fpm/conf.d/10-opcache.ini && \
    echo "opcache.revalidate_freq=60" >> /etc/php/7.1/fpm/conf.d/10-opcache.ini

# Add Scripts
ADD scripts/start.sh /start.sh
RUN chmod 755 /start.sh

# copy in code and errors
# ADD src/ /var/www/html/
ADD errors/ /var/www/errors

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php -r "if (hash_file('SHA384', 'composer-setup.php') === '${composer_hash}') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" && \
    php composer-setup.php --install-dir=/usr/bin --filename=composer && \
    php -r "unlink('composer-setup.php');"

#ADD https://releases.hashicorp.com/consul-template/0.18.0/consul-template_0.18.0_SHA256SUMS /tmp/
#ADD https://releases.hashicorp.com/consul-template/0.18.0/consul-template_0.18.0_linux_amd64.zip /tmp/

#RUN cd /tmp && \
#    sha256sum -c consul-template_0.18.0_SHA256SUMS 2>&1 | grep OK && \
#    unzip consul-template_0.18.0_linux_amd64.zip && \
#    mv consul-template /bin/consul-template && \
#    rm -rf /tmp/*

EXPOSE 80

CMD ["/start.sh"]
