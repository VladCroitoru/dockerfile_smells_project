###################################
# Nginx Centos7
# Mount volume
#     site code
#         /var/www/
#     site config
#         /etc/nginx/conf.d/
#     ADD default.conf /etc/nginx/conf.d/default.conf
# Refer: 
#    http://tecadmin.net/install-php-7-nginx-mysql-5-on-centos/
#    https://github.com/million12/docker-nginx-php
#    https://github.com/million12/docker-nginx
#    Nginx tuning
#    https://github.com/iiiepe/docker-nginx-drupal6
#    https://hub.docker.com/r/iiiepe/nginx-drupal6
# Build
#    docker build -t kanalfred/nginx7 .
# Run: 
#   docker run -h nginx7 --name nginx7 -p 2200:22 -p 80:80 -p 443:443 -d kanalfred/nginx7 
#   docker run -h nginx7 --name nginx7 -p 2200:22 -p 80:80 -p 443:443 -d -v /data/nginx/etc/nginx/conf.d:/etc/nginx/conf.d -v /data/nginx/var/www/apple:/var/www/apple -v /data/nginx/var/www/wvpn:/var/www/wvpn kanalfred/nginx7
#   docker run -h nginx7 --name nginx7 -p 2200:22 -p 80:80 -p 443:443 -d -v /data/nginx/data:/data kanalfred/nginx7
#   docker run -e 'apple=asfa!sdfaboy!' -h nginx7 --name nginx7 -p 2200:22 -p 80:80 -p 443:443 -d -v /data/nginx/data:/data kanalfred/nginx7
#
###################################

FROM kanalfred/centos7:latest

MAINTAINER Alfred Kan <kanalfred@gmail.com>

# Add Files
ADD container-files /

# User
RUN adduser --uid 1000 hostadmin \
        && cat /root/hostadmin.txt | passwd hostadmin --stdin

#RUN mkdir /data
VOLUME ["/data"]

# PHP7
RUN \
    # Install PHP 7.0 from Remi Enterprise YUM repository
    #rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm && \
    rpm -Uvh /tmp/remi-release-7.rpm && \

    # Install php7 module
    yum install -y \
        php70-php \
        php70-php-bcmath \
        php70-php-cli \
        php70-php-common \
        php70-php-devel \
        php70-php-fpm \
        php70-php-gd \
        php70-php-gmp \
        php70-php-intl \
        php70-php-json \
        php70-php-mbstring \
        php70-php-mcrypt \
        php70-php-mysqlnd \
        php70-php-opcache \
        php70-php-pdo \
        php70-php-pear \
        php70-php-process \
        php70-php-pspell \
        php70-php-xml \

        # Also install the following PECL packages
        php70-php-pecl-imagick \
        php70-php-pecl-mysql \
        php70-php-pecl-uploadprogress \
        php70-php-pecl-uuid \
        php70-php-pecl-zip && \

    # Set PATH so it includes newest PHP and its aliases...
    ln -sfF /opt/remi/php70/enable /etc/profile.d/php70-paths.sh && \
    # The above will set PATH when container starts... but not when php is used on container build time
    # Therefore create symlinks in /usr/local/bin for all PHP tools...
    ln -sfF /opt/remi/php70/root/usr/bin/{pear,pecl,phar,php,php-cgi,php-config,phpize} /usr/local/bin/. && \

    php --version && \

    # Move PHP config files from /etc/opt/remi/php70/* to /etc/* 
    mv -f /etc/opt/remi/php70/php.ini /etc/php.ini && ln -s /etc/php.ini /etc/opt/remi/php70/php.ini && \
    rm -rf /etc/php.d && mv /etc/opt/remi/php70/php.d /etc/. && ln -s /etc/php.d /etc/opt/remi/php70/php.d && \
    echo 'PHP 7 installed.' && \
	
    # Install Composer
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    chown hostadmin /usr/local/bin/composer && composer --version && \
    composer config -g secure-http false

# Ngnix
#ENV DOCKERIZE_VERSION v0.2.0

RUN \
    # Install nginx
    yum install -y nginx && \

    # Add user hostadmin to groups
    usermod -a -G nginx hostadmin && \
    usermod -a -G apache hostadmin
    
    # Install dockerize - replace env var in config file
    #wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    #&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz	

ADD container-files /

# Wrap up
RUN \
    # Remove pass file
    rm -f /root/hostadmin.txt && \

    # Clean YUM caches to minimise Docker image size... 
    yum clean all && rm -rf /tmp/yum*


EXPOSE 80 443

# start all register services
CMD dockerize -template /tmp/test.conf:/tmp/test.conf /config/run.sh
#CMD ["/config/run.sh"]

